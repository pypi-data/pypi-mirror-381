"""Test raw file metadata recording functionality."""
from __future__ import annotations
import tempfile
import csv
from pathlib import Path
import datetime as dt
import hashlib

import pandas as pd
import pytest

from provolone import load, load_with_metadata
from provolone.utils.file_meta import extract_file_metadata
from provolone.utils.hash import hash_file


def test_file_meta_extraction():
    """Test the extract_file_metadata utility function."""
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '1.0'])
        writer.writerow(['2024-02-01', '2.0'])
        temp_path = Path(f.name)
    
    try:
        # Test basic file metadata extraction
        meta = extract_file_metadata(temp_path)
        
        # Check all expected fields are present
        assert 'raw_file_path' in meta
        assert 'raw_file_name' in meta
        assert 'raw_file_size' in meta
        assert 'raw_file_mtime' in meta
        assert 'raw_file_sha256' in meta
        assert 'raw_file_exists' in meta
        assert 'raw_file_type' in meta
        
        # Check field values
        assert meta['raw_file_path'] == str(temp_path.absolute())
        assert meta['raw_file_name'] == temp_path.name
        assert meta['raw_file_exists'] is True
        assert meta['raw_file_type'] == 'csv'
        assert meta['raw_file_size'] > 0
        assert len(meta['raw_file_sha256']) == 64  # Full SHA256 hash
        
        # Check mtime is valid ISO8601
        dt.datetime.fromisoformat(meta['raw_file_mtime'])
        
        # Test with user-provided url and notes
        meta_with_extras = extract_file_metadata(
            temp_path,
            url="https://example.com/data.csv",
            notes="Test data for unit tests"
        )
        
        assert meta_with_extras['raw_file_url'] == "https://example.com/data.csv"
        assert meta_with_extras['raw_file_notes'] == "Test data for unit tests"
        
    finally:
        temp_path.unlink()  # Clean up


def test_file_meta_nonexistent_file():
    """Test file metadata extraction for nonexistent file."""
    nonexistent = Path("/tmp/does_not_exist.csv")
    meta = extract_file_metadata(nonexistent)
    
    assert meta['raw_file_exists'] is False
    assert meta['raw_file_path'] == str(nonexistent.absolute())
    assert meta['raw_file_name'] == "does_not_exist.csv"
    # Should not have size, mtime, or sha256 for nonexistent files
    assert 'raw_file_size' not in meta
    assert 'raw_file_mtime' not in meta
    assert 'raw_file_sha256' not in meta


def test_raw_file_metadata_in_load_with_file(tmp_path):
    """Test that raw file metadata is recorded when loading dataset with real file."""
    # Create example CSV file
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
        writer.writerow(['2024-02-01', '20.0'])
        writer.writerow(['2024-03-01', '30.0'])
    
    # Load dataset with user-provided metadata using data_root parameter
    df, meta = load_with_metadata(
        "example", 
        force=True,
        data_root=str(tmp_path),
        raw_file_url="https://data-provider.com/example.csv",
        raw_file_notes="Downloaded from provider portal on 2024-12-27"
    )
    
    # Check that raw files metadata was recorded (now as a list)
    assert 'raw_files' in meta
    assert isinstance(meta['raw_files'], list)
    assert len(meta['raw_files']) == 1
    
    # Get the single file metadata from the list
    raw_meta = meta['raw_files'][0]
    
    # Check all expected fields
    assert raw_meta['raw_file_path'] == str(csv_file.absolute())
    assert raw_meta['raw_file_name'] == 'example.csv'
    assert raw_meta['raw_file_exists'] is True
    assert raw_meta['raw_file_type'] == 'csv'
    assert raw_meta['raw_file_size'] > 0
    assert len(raw_meta['raw_file_sha256']) == 64
    
    # Check user-provided metadata
    assert raw_meta['raw_file_url'] == "https://data-provider.com/example.csv"
    assert raw_meta['raw_file_notes'] == "Downloaded from provider portal on 2024-12-27"
    
    # Verify hash matches actual file content
    expected_hash = hash_file(csv_file, truncate=False)
    assert raw_meta['raw_file_sha256'] == expected_hash
    
    # Verify mtime is valid
    dt.datetime.fromisoformat(raw_meta['raw_file_mtime'])
    
    # Check that the DataFrame was loaded correctly 
    assert len(df) == 3
    assert list(df.columns) == ['value']
    assert df.index.name == 'date'


def test_raw_file_metadata_no_file(tmp_path):
    """Test that no raw file metadata is recorded when no file is used."""
    # Load dataset with no file (using fallback data) - pass data_root even though no file exists
    df, meta = load_with_metadata("example", force=True, data_root=str(tmp_path))
    
    # Should not have raw file metadata since no file was used
    assert 'raw_files' not in meta
    
    # Check that the fallback DataFrame was loaded correctly
    assert len(df) == 3
    assert list(df.columns) == ['value']
    assert df.index.name == 'date'


def test_raw_file_metadata_persists_in_cache(tmp_path):
    """Test that raw file metadata is preserved when loading from cache."""
    # Create example CSV file
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
    
    # Use snapshot_dir to control cache location
    cache_dir = tmp_path / "cache"
    
    # First load - should compute fresh and record metadata
    df1, meta1 = load_with_metadata(
        "example", 
        force=True,
        data_root=str(tmp_path),
        snapshot_dir=str(cache_dir),
        raw_file_url="https://test.com/data.csv"
    )
    assert meta1['cache'] == 'miss'
    assert 'raw_files' in meta1
    assert len(meta1['raw_files']) == 1
    assert meta1['raw_files'][0]['raw_file_url'] == "https://test.com/data.csv"
    
    # Second load - should hit cache and preserve metadata
    df2, meta2 = load_with_metadata(
        "example",
        data_root=str(tmp_path),
        snapshot_dir=str(cache_dir)
    )
    assert meta2['cache'] == 'hit'
    assert 'raw_files' in meta2
    assert len(meta2['raw_files']) == 1
    assert meta2['raw_files'][0]['raw_file_url'] == "https://test.com/data.csv"
    
    # Verify DataFrames are identical
    pd.testing.assert_frame_equal(df1, df2)


def test_raw_file_metadata_in_snapshot(tmp_path):
    """Test that raw file metadata is preserved in snapshots."""
    from provolone import freeze
    from provolone.snapshots import read_snapshot
    
    # Create example CSV file
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '100.0'])
    
    # Use global snapshot dir for test (backward compatible with old root-based behavior)
    import os
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(tmp_path / "snapshots")
    
    # Create snapshot with metadata
    snapshot_path = freeze(
        "example", 
        snapshot="test-snapshot",
        data_root=str(tmp_path),
        raw_file_url="https://example.org/snapshot-data.csv",
        raw_file_notes="Frozen for reproducible analysis",
        force=True
    )
    
    # Read snapshot and verify metadata is preserved
    df, meta = read_snapshot("example", "test-snapshot")
    
    assert 'raw_files' in meta
    assert len(meta['raw_files']) == 1
    raw_meta = meta['raw_files'][0]
    assert raw_meta['raw_file_url'] == "https://example.org/snapshot-data.csv"
    assert raw_meta['raw_file_notes'] == "Frozen for reproducible analysis"
    assert raw_meta['raw_file_name'] == 'example.csv'
    assert raw_meta['raw_file_exists'] is True


def test_raw_file_metadata_error_handling(tmp_path, monkeypatch):
    """Test that metadata extraction errors don't break dataset loading."""
    # Mock extract_file_metadata to raise an error
    from provolone.utils import file_meta
    
    def failing_extract(*args, **kwargs):
        raise OSError("Permission denied")
    
    monkeypatch.setattr(file_meta, "extract_file_metadata", failing_extract)
    
    # Create example CSV file
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
    
    # Load should succeed even though metadata extraction fails
    df, meta = load_with_metadata("example", force=True, data_root=str(tmp_path))
    
    # Should not have raw file metadata due to the error
    assert 'raw_files' not in meta
    
    # But the DataFrame should still load correctly (1 data row)
    assert len(df) == 1
    assert list(df.columns) == ['value']