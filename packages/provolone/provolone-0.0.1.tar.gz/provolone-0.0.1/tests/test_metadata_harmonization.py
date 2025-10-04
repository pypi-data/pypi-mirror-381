"""
Test metadata harmonization - ensuring standard metadata is saved and loaded with all dataframes.
"""


def test_cache_metadata_consistency(tmp_path, monkeypatch):
    """Test that cache operations save and load standardized metadata."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    from provolone import load_with_metadata

    # Load dataset which will write to cache
    df, meta = load_with_metadata("example", force=True)

    # Verify standardized metadata fields are present
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
    assert expected_fields.issubset(
        set(meta.keys())
    ), f"Missing fields: {expected_fields - set(meta.keys())}"

    # Load again from cache - should have same metadata structure with different cache status
    df2, meta2 = load_with_metadata("example", force=False)

    assert meta2["cache"] == "hit"
    assert meta2["content_hash"] == meta["content_hash"]  # Should be same content
    assert meta2["dataset"] == meta["dataset"]  # Should be same dataset


def test_snapshot_metadata_consistency(tmp_path, monkeypatch):
    """Test that snapshots use standardized metadata."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_ROOT", str(tmp_path / "snapshots"))
    from provolone import freeze, load_with_metadata

    # Create snapshot
    freeze("example", snapshot="test-meta", force=True)

    # Load from snapshot
    df, meta = load_with_metadata("example", snapshot="test-meta")

    # Verify standardized metadata fields are present
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
    assert expected_fields.issubset(
        set(meta.keys())
    ), f"Missing fields: {expected_fields - set(meta.keys())}"

    assert meta["cache"] == "snapshot-hit"
    assert meta["dataset"] == "example"
    assert meta["content_hash"] is not None


def test_metadata_file_creation(tmp_path, monkeypatch):
    """Test that metadata files are created alongside data files."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_ROOT", str(tmp_path / "snapshots"))
    from provolone import load_with_metadata
    from provolone.config import cfg
    import json

    # Load dataset which creates cache files
    df, meta = load_with_metadata("example", force=True)

    # With the new system, cache files go to snapshot_dir/dataset/_default/
    # Since the config is cached, check where files actually ended up
    expected_cache_dir = tmp_path / "snapshots" / "example" / "_default"

    # If the snapshot_dir wasn't properly updated due to config caching,
    # fall back to the actual config location
    if not expected_cache_dir.exists():
        # Check the actual config location
        from pathlib import Path

        actual_snapshot_dir = Path(cfg.snapshots_root)
        expected_cache_dir = actual_snapshot_dir / "example" / "_default"

    data_files = (
        list(expected_cache_dir.glob("data.*")) if expected_cache_dir.exists() else []
    )
    # With consolidated metadata, we only have .meta.json files (no more .data.meta.json)
    meta_files = (
        list(expected_cache_dir.glob("*.meta.json"))
        if expected_cache_dir.exists()
        else []
    )

    assert (
        len(data_files) >= 1
    ), f"Data file should exist, found files: {list(expected_cache_dir.iterdir()) if expected_cache_dir.exists() else 'directory does not exist'}"
    assert len(meta_files) == 1, "Consolidated metadata file should exist"

    # Check metadata file content (now contains both data and index metadata)
    meta_file = meta_files[0]
    with open(meta_file) as f:
        file_meta = json.load(f)

    # Verify key fields are in the consolidated file
    assert "content_hash" in file_meta
    assert "dataset" in file_meta
    assert "created_at" in file_meta
    assert "index" in file_meta  # Index metadata should be included
    assert "index_cols" in file_meta  # For backward compatibility
    assert file_meta["dataset"] == "example"
