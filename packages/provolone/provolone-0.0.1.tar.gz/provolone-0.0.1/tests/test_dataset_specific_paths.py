"""
Test dataset-specific data_root and snapshot_dir configuration
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import subprocess
import sys


def run_isolated_test(test_code):
    """Run test code in a separate Python process to avoid config caching."""
    script = f"""
import tempfile
from pathlib import Path
import os
import sys

{test_code}
"""
    result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True)
    if result.returncode != 0:
        pytest.fail(f"Test failed with stderr: {result.stderr}")
    return result.stdout


def test_dataset_specific_data_root():
    """Test that datasets can use custom data_dir pointing directly to dataset directory."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    global_data_root = tmp_path / "global_data"
    custom_example_dir = tmp_path / "custom_example_data" 
    snapshot_dir = tmp_path / "snapshots"
    
    for p in [global_data_root, custom_example_dir, snapshot_dir]:
        p.mkdir()
    
    # Create test data files with global data_root structure (data_root/example/...)
    (global_data_root / "example").mkdir()
    (global_data_root / "example" / "example.csv").write_text("date,value\\n2020-01-01,1\\n2020-02-01,2\\n")
    
    # Create test data file with direct dataset directory (no example/ subdirectory)
    (custom_example_dir / "example.csv").write_text("date,value\\n2021-01-01,10\\n2021-02-01,20\\n")
    
    # Set global configuration
    os.environ["PROVOLONE_DATA_ROOT"] = str(global_data_root)
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(snapshot_dir)
    
    import provolone
    
    # Test loading with global data_root (uses global config with example/ subdirectory)
    df_global = provolone.load("example", force=True)
    assert len(df_global) == 2
    assert df_global.iloc[0]["value"] == 1  # From global data
    
    # Test loading with custom data_dir (points directly to dataset directory)
    df_custom = provolone.load("example", data_dir=custom_example_dir, force=True)
    assert len(df_custom) == 2
    assert df_custom.iloc[0]["value"] == 10  # From custom data
    
    # Verify they're different
    assert not df_global.equals(df_custom)
    print("SUCCESS: Dataset specific data_dir working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_dataset_specific_snapshot_dir():
    """Test that datasets can use custom snapshot_dir pointing directly to dataset's snapshot directory."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    global_snapshots = tmp_path / "global_snapshots"
    custom_example_snapshots = tmp_path / "custom_example_snapshots"
    
    for p in [global_snapshots, custom_example_snapshots]:
        p.mkdir()
    
    # Set up global config
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(global_snapshots)
    
    import provolone
    
    # Create a snapshot with global snapshot_dir (uses global/example/label structure)
    provolone.freeze("example", snapshot="test_global")
    assert (global_snapshots / "example" / "test_global").exists()
    
    # Create a snapshot with custom snapshot_dir (points directly to dataset's snapshots)
    provolone.freeze("example", snapshot="test_custom", snapshot_dir=custom_example_snapshots)
    # With dataset-specific path, snapshot is stored directly under snapshot_dir/label
    assert (custom_example_snapshots / "test_custom").exists()
    assert not (custom_example_snapshots / "example").exists()
    
    # Load from global snapshot
    df_global = provolone.load("example", snapshot="test_global")
    
    # Load from custom snapshot
    df_custom = provolone.load("example", snapshot="test_custom", snapshot_dir=custom_example_snapshots)
    
    # They should be the same data but from different locations
    assert df_global.equals(df_custom)
    print("SUCCESS: Dataset specific snapshot_dir working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_dataset_specific_cache_isolation():
    """Test that datasets with different snapshot_dir have isolated caches."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    snapshots_a = tmp_path / "snapshots_a"
    snapshots_b = tmp_path / "snapshots_b"
    
    for p in [snapshots_a, snapshots_b]:
        p.mkdir()
    
    # Set a global fallback
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(tmp_path / "global")
    
    import provolone
    
    # Load with different snapshot_dir - should create separate caches
    # With dataset-specific paths, caches are stored directly under snapshot_dir
    df_a = provolone.load("example", snapshot_dir=snapshots_a)
    df_b = provolone.load("example", snapshot_dir=snapshots_b)
    
    # Verify separate cache locations exist (they will have different hashed suffixes)
    # Caches are now stored directly under snapshot_dir with _default__ prefix
    cache_dirs_a = list(snapshots_a.iterdir())
    cache_dirs_b = list(snapshots_b.iterdir())
    
    assert len(cache_dirs_a) == 1, f"Expected 1 cache dir in A, got {len(cache_dirs_a)}"
    assert len(cache_dirs_b) == 1, f"Expected 1 cache dir in B, got {len(cache_dirs_b)}"
    
    # Cache directory names should be different due to path hashing
    cache_name_a = cache_dirs_a[0].name
    cache_name_b = cache_dirs_b[0].name
    assert cache_name_a != cache_name_b, f"Cache names should be different: {cache_name_a} vs {cache_name_b}"
    
    # Both should start with _default__ (indicating cache isolation)
    assert cache_name_a.startswith("_default__")
    assert cache_name_b.startswith("_default__")
    
    # Data should be the same (since it's the same dataset)
    assert df_a.equals(df_b)
    print("SUCCESS: Cache isolation working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_backward_compatibility():
    """Test that existing code without custom paths still works."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    snapshot_dir = tmp_path / "snapshots"
    snapshot_dir.mkdir()
    
    # Set global config
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(snapshot_dir)
    
    import provolone
    
    # Old API should work without any path parameters
    df = provolone.load("example")
    assert len(df) == 3  # fallback data has 3 rows
    
    # Creating snapshots should work
    provolone.freeze("example", snapshot="test_compat")
    
    # Loading snapshots should work
    df_snap = provolone.load("example", snapshot="test_compat")
    assert df.equals(df_snap)
    print("SUCCESS: Backward compatibility working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_load_with_metadata_custom_paths():
    """Test load_with_metadata with custom paths."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    custom_snapshots = tmp_path / "custom"
    custom_snapshots.mkdir()
    
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(tmp_path / "global")
    
    import provolone
    
    # Create snapshot with custom path
    provolone.freeze("example", snapshot="meta_test", snapshot_dir=custom_snapshots)
    
    # Load with metadata using custom path
    df, meta = provolone.load_with_metadata("example", snapshot="meta_test", snapshot_dir=custom_snapshots)
    
    assert len(df) == 3  # fallback data
    assert meta["cache"] == "snapshot-hit"
    assert "snapshot_dir" in meta["params"]  # Should preserve the parameter
    print("SUCCESS: load_with_metadata with custom paths working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_example_dataset_properties():
    """Test that datasets correctly expose data_dir and snapshot_dir properties."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    custom_data = tmp_path / "custom_data"
    custom_snapshots = tmp_path / "custom_snapshots"
    global_data = tmp_path / "global_data"
    global_snapshots = tmp_path / "global_snapshots"
    
    for p in [custom_data, custom_snapshots, global_data, global_snapshots]:
        p.mkdir()
    
    # Set global config
    os.environ["PROVOLONE_DATA_ROOT"] = str(global_data)
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(global_snapshots)
    
    from provolone.datasets import get
    
    # Dataset with global config (appends dataset name to global paths)
    ds_global = get("example")()
    assert ds_global.data_dir == global_data / "example"
    assert ds_global.snapshot_dir == global_snapshots / "example"
    
    # Dataset with custom paths (uses paths directly, no name appended)
    ds_custom = get("example")(data_dir=custom_data, snapshot_dir=custom_snapshots)
    assert ds_custom.data_dir == custom_data
    assert ds_custom.snapshot_dir == custom_snapshots
    print("SUCCESS: Dataset properties working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output