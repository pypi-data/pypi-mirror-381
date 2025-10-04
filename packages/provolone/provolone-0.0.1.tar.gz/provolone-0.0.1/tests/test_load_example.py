def test_load_example_roundtrip(tmp_path, monkeypatch):
    # Make provolone write cache into a temp dir
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    from provolone import load

    df = load("example", force=True)
    assert not df.empty
    assert "value" in df.columns
    # Ensure second load reads from cache (should be identical)
    df2 = load("example", force=False)
    assert df2.equals(df)


def test_load_with_metadata_example(tmp_path, monkeypatch):
    """Test the new load_with_metadata function."""
    # Make provolone write cache into a temp dir
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    from provolone import load_with_metadata, load

    # Test fresh computation
    df, meta = load_with_metadata("example", force=True)
    assert not df.empty
    assert "value" in df.columns
    assert isinstance(meta, dict)
    assert "params" in meta
    assert "cache" in meta
    assert meta["cache"] == "miss"  # First load should be a cache miss
    assert "content_hash" in meta

    # Test cached load
    df2, meta2 = load_with_metadata("example", force=False)
    assert df2.equals(df)
    assert meta2["cache"] == "hit"  # Second load should be a cache hit
    assert (
        "content_hash" in meta2
    )  # Cache hits now include hash from standardized metadata

    # Compare with regular load function
    df3 = load("example")
    assert df3.equals(df)


def test_load_with_metadata_with_params(tmp_path, monkeypatch):
    """Test load_with_metadata with custom parameters."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    from provolone import load_with_metadata

    # Test with some dummy parameters (example dataset might ignore them)
    df, meta = load_with_metadata("example", force=True, dummy_param="test_value")
    assert not df.empty
    assert meta["params"]["dummy_param"] == "test_value"


def test_load_with_metadata_snapshot(tmp_path, monkeypatch):
    """Test load_with_metadata with snapshots."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_ROOT", str(tmp_path / "snapshots"))
    from provolone import load_with_metadata, freeze

    # First create a snapshot
    freeze("example", snapshot="test_snapshot", force=True)

    # Load from snapshot
    df, meta = load_with_metadata("example", snapshot="test_snapshot")
    assert not df.empty
    assert meta["cache"] == "snapshot-hit"
    assert "params" in meta
