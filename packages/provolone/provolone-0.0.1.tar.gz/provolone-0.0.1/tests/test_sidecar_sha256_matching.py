"""Test SHA256 matching for sidecar metadata preservation."""
from __future__ import annotations
import csv
import shutil
from pathlib import Path
import tempfile
import json

import pytest

from provolone import tag, load_with_metadata
from provolone.utils.file_meta import extract_file_metadata


def test_extract_file_metadata_with_matching_sidecar():
    """Test that extract_file_metadata preserves sidecar metadata when SHA256 matches."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n")
        f.flush()
        file_path = Path(f.name)

        try:
            # Create sidecar metadata file
            sidecar_meta = {
                "raw_file_path": "/original/path/data.csv",
                "raw_file_name": "data.csv", 
                "raw_file_exists": True,
                "raw_file_size": 999,  # Different from actual size
                "raw_file_mtime": "2024-01-01T12:00:00+00:00",  # Different from actual mtime
                "raw_file_sha256": None,  # Will be set to actual SHA256
                "raw_file_type": "csv",
                "raw_file_url": "https://original.com/data.csv",
                "raw_file_notes": "Original acquisition metadata"
            }

            # First extract metadata to get the actual SHA256
            actual_meta = extract_file_metadata(file_path)
            sidecar_meta["raw_file_sha256"] = actual_meta["raw_file_sha256"]

            # Now extract with sidecar metadata
            result = extract_file_metadata(file_path, sidecar_meta=sidecar_meta)

            # Should have preserved original metadata
            assert result["raw_file_sha256_match"] is True
            assert result["raw_file_path"] == "/original/path/data.csv"
            assert result["raw_file_size"] == 999
            assert result["raw_file_mtime"] == "2024-01-01T12:00:00+00:00"
            assert result["raw_file_url"] == "https://original.com/data.csv" 
            assert result["raw_file_notes"] == "Original acquisition metadata"

            # Should have current runtime context
            assert result["file_at_load_path"] == str(file_path.absolute())
            assert result["file_at_load_name"] == file_path.name
            assert result["file_at_load_exists"] is True
            assert result["file_at_load_sha256"] == actual_meta["raw_file_sha256"]
            assert "file_at_load_size" in result
            assert "file_at_load_mtime" in result

            # Should have debug fields
            assert result["raw_file_sidecar_sha256"] == actual_meta["raw_file_sha256"]

        finally:
            file_path.unlink(missing_ok=True)


def test_extract_file_metadata_with_mismatched_sidecar():
    """Test that extract_file_metadata recomputes metadata when SHA256 doesn't match."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n")
        f.flush()
        file_path = Path(f.name)

        try:
            # Create sidecar metadata with wrong SHA256
            sidecar_meta = {
                "raw_file_path": "/original/path/data.csv",
                "raw_file_name": "data.csv",
                "raw_file_sha256": "wrong_hash_value",
                "raw_file_url": "https://original.com/data.csv",
                "raw_file_notes": "Original acquisition metadata"
            }

            # Extract with mismatched sidecar metadata
            result = extract_file_metadata(file_path, sidecar_meta=sidecar_meta)

            # Should have recomputed metadata, not preserved sidecar
            assert result["raw_file_sha256_match"] is False
            assert result["raw_file_path"] == str(file_path.absolute())  # Current path, not original
            assert result["raw_file_name"] == file_path.name  # Current name, not original

            # Should still have runtime context
            assert result["file_at_load_path"] == str(file_path.absolute())
            assert "file_at_load_sha256" in result

            # Should have debug fields
            assert result["raw_file_sidecar_sha256"] == "wrong_hash_value"

        finally:
            file_path.unlink(missing_ok=True)


def test_extract_file_metadata_no_sidecar():
    """Test that extract_file_metadata works normally when no sidecar is provided."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n")
        f.flush()
        file_path = Path(f.name)

        try:
            # Extract without sidecar metadata
            result = extract_file_metadata(file_path, url="https://test.com", notes="Test notes")

            # Should have recomputed metadata
            assert result["raw_file_sha256_match"] is False
            assert result["raw_file_path"] == str(file_path.absolute())
            assert result["raw_file_url"] == "https://test.com"
            assert result["raw_file_notes"] == "Test notes"

            # Should have runtime context
            assert result["file_at_load_path"] == str(file_path.absolute())
            assert "file_at_load_sha256" in result

            # Should not have sidecar debug field
            assert "raw_file_sidecar_sha256" not in result

        finally:
            file_path.unlink(missing_ok=True)


def test_file_copy_preserves_sidecar_metadata(tmp_path):
    """Test that copying a file with sidecar preserves original metadata when SHA256 matches."""
    # Create original file
    original_dir = tmp_path / "original"
    original_dir.mkdir()
    original_file = original_dir / "data.csv"
    
    with open(original_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")
    
    # Create sidecar metadata for original
    meta_path = tag(
        str(original_file),
        raw_file_url="https://original-source.com/data.csv",
        raw_file_notes="Downloaded from original source"
    )
    
    # Copy file and sidecar to new location
    copy_dir = tmp_path / "copy"
    copy_dir.mkdir()
    copy_file = copy_dir / "data.csv"
    copy_meta = copy_dir / "data.meta.json"
    
    shutil.copy2(original_file, copy_file)
    shutil.copy2(meta_path, copy_meta)
    
    # Now create a dataset structure to test loading
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    example_file = example_dir / "example.csv"
    example_meta = example_dir / "example.meta.json"
    
    shutil.copy2(copy_file, example_file)
    shutil.copy2(copy_meta, example_meta)
    
    # Load the dataset - should preserve original metadata
    df, meta = load_with_metadata("example", force=True, data_root=str(tmp_path))
    
    # Check that original metadata was preserved (now in raw_files list)
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    
    assert raw_meta["raw_file_sha256_match"] is True
    assert raw_meta["raw_file_url"] == "https://original-source.com/data.csv"
    assert raw_meta["raw_file_notes"] == "Downloaded from original source"
    assert raw_meta["raw_file_path"] == str(original_file.absolute())  # Original path preserved
    
    # Should have current runtime context
    assert raw_meta["file_at_load_path"] == str(example_file.absolute())
    assert raw_meta["file_at_load_exists"] is True
    assert "file_at_load_mtime" in raw_meta
    assert "file_at_load_size" in raw_meta


def test_file_modified_after_tagging_recomputes_metadata(tmp_path):
    """Test that modifying a file after tagging causes metadata to be recomputed."""
    # Create example dataset structure
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    # Create initial file
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n")
    
    # Create sidecar metadata
    meta_path = tag(
        str(csv_file),
        raw_file_url="https://original-source.com/data.csv",
        raw_file_notes="Original metadata"
    )
    
    # Load original metadata to get SHA256
    with open(meta_path) as f:
        original_meta = json.load(f)
    original_sha256 = original_meta["raw_file_sha256"]
    
    # Modify the file (different content = different SHA256)
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")  # Added more data
    
    # Load the dataset - should recompute metadata due to SHA256 mismatch
    df, meta = load_with_metadata("example", force=True, data_root=str(tmp_path))
    
    # Check that metadata was recomputed (now in raw_files list)
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    
    assert raw_meta["raw_file_sha256_match"] is False
    assert raw_meta["raw_file_sidecar_sha256"] == original_sha256
    assert raw_meta["raw_file_sha256"] != original_sha256  # Should be different
    assert raw_meta["raw_file_path"] == str(csv_file.absolute())  # Current path
    
    # Source and notes should still be defaulted from sidecar
    assert raw_meta["raw_file_url"] == "https://original-source.com/data.csv"
    assert raw_meta["raw_file_notes"] == "Original metadata"


def test_user_params_override_preserved_sidecar_metadata(tmp_path):
    """Test that sidecar metadata takes precedence over user params."""
    # Create example dataset structure
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n")
    
    # Create sidecar metadata
    tag(
        str(csv_file),
        raw_file_url="https://sidecar-source.com/data.csv",
        raw_file_notes="Sidecar metadata"
    )
    
    # Load with params - sidecar should take precedence
    df, meta = load_with_metadata(
        "example", 
        force=True, 
        data_root=str(tmp_path),
        raw_file_url="https://user-override.com/data.csv",
        raw_file_notes="User provided notes"
    )
    
    # Check that sidecar metadata took precedence (now in raw_files list)
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    
    assert raw_meta["raw_file_sha256_match"] is True  # SHA256 should still match
    # Sidecar metadata should be used, not params
    assert raw_meta["raw_file_url"] == "https://sidecar-source.com/data.csv"
    assert raw_meta["raw_file_notes"] == "Sidecar metadata"