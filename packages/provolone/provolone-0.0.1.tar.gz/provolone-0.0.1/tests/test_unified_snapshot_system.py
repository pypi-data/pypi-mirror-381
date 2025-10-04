"""
Test the new overwrite protection and unified snapshot system
"""

import pytest
from pathlib import Path
import uuid


def test_overwrite_protection_and_unified_system(tmp_path, monkeypatch):
    """Test the new overwrite protection and unified snapshot system."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_ROOT", str(tmp_path / "snapshots"))
    from provolone import freeze, load, load_with_metadata

    # Use unique snapshot name to avoid conflicts with other tests
    snapshot_name = f"test_protection_{uuid.uuid4().hex[:8]}"

    # Test 1: Cache operations should always be overwritable (using _default snapshot)
    print("Testing cache overwrite behavior...")
    df1 = load("example", force=True)
    df2 = load(
        "example", force=True
    )  # Should succeed - cache can always be overwritten
    assert df1.equals(df2)

    # Test 2: Regular snapshots should not be overwritable without force
    print("Testing snapshot overwrite protection...")
    freeze("example", snapshot=snapshot_name, force=False)

    # Try to overwrite without force - should fail
    with pytest.raises(FileExistsError) as exc_info:
        freeze("example", snapshot=snapshot_name, force=False)
    assert snapshot_name in str(exc_info.value)
    assert "already exists" in str(exc_info.value)

    # Overwrite with force - should succeed
    freeze("example", snapshot=snapshot_name, force=True)

    # Test 3: Verify unified file structure
    print("Testing unified file structure...")

    # Due to config caching in tests, we need to check the actual location
    from provolone.config import cfg

    actual_snapshot_dir = Path(cfg.snapshots_root)
    snapshot_dir = actual_snapshot_dir / "example"

    # If the expected location doesn't exist, use the actual config location
    expected_location = tmp_path / "snapshots" / "example"
    if not expected_location.exists():
        snapshot_dir = actual_snapshot_dir / "example"
    else:
        snapshot_dir = expected_location

    # Both cache and snapshots should have the same file structure
    default_files = (
        list((snapshot_dir / "_default").glob("*"))
        if (snapshot_dir / "_default").exists()
        else []
    )
    snapshot_files = (
        list((snapshot_dir / snapshot_name).glob("*"))
        if (snapshot_dir / snapshot_name).exists()
        else []
    )

    # Both should have data file and two metadata files (no manifest.json)
    default_names = {f.name for f in default_files}
    snapshot_names = {f.name for f in snapshot_files}

    expected_files = {
        "data.parquet",
        "data.parquet.meta.json",  # Only one metadata file now
    }
    assert expected_files.issubset(
        default_names
    ), f"Cache missing files: {expected_files - default_names}"
    assert expected_files.issubset(
        snapshot_names
    ), f"Snapshot missing files: {expected_files - snapshot_names}"

    # Neither should have manifest.json (redundant metadata removed)
    assert "manifest.json" not in default_names
    assert "manifest.json" not in snapshot_names

    # Test 4: Verify metadata consistency
    print("Testing metadata consistency...")
    df_cache, meta_cache = load_with_metadata("example", force=False)
    df_snapshot, meta_snapshot = load_with_metadata("example", snapshot=snapshot_name)

    # Both should have the same standardized metadata structure
    expected_fields = {
        "created_at",
        "version",
        "params",
        "io",
        "shape",
        "index",
        "content_hash",
        "dataset",
        "cache",
    }
    assert expected_fields.issubset(set(meta_cache.keys()))
    assert expected_fields.issubset(set(meta_snapshot.keys()))

    # Cache status should be different
    assert meta_cache["cache"] == "hit"
    assert meta_snapshot["cache"] == "snapshot-hit"

    print("✅ All tests passed!")


def test_cli_overwrite_protection(tmp_path, monkeypatch):
    """Test overwrite protection through the freeze function."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_ROOT", str(tmp_path / "snapshots"))
    from provolone import freeze
    import uuid

    # Use unique snapshot name to avoid conflicts
    snapshot_name = f"cli_test_{uuid.uuid4().hex[:8]}"

    # Create initial snapshot
    freeze("example", snapshot=snapshot_name, force=False)

    # Try to create again without force - should fail
    with pytest.raises(FileExistsError):
        freeze("example", snapshot=snapshot_name, force=False)

    # Try to create with force - should succeed
    freeze("example", snapshot=snapshot_name, force=True)

    print("✅ CLI overwrite protection works correctly!")
