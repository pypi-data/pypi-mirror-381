"""
Test that data_dir and snapshot_dir can be passed as direct arguments
to load/freeze API functions and CLI commands, falling back to params.
"""

import pytest
from pathlib import Path
import tempfile
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


def test_load_with_direct_data_dir_argument():
    """Test that load() accepts data_dir as direct argument."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    custom_example_data = tmp_path / "custom_example_data"
    custom_example_data.mkdir()
    
    # Create test data file directly in the dataset directory
    (custom_example_data / "example.csv").write_text("date,value\\n2021-01-01,100\\n2021-02-01,200\\n")
    
    import provolone
    
    # Load with direct data_dir argument (points to dataset directory)
    df = provolone.load("example", data_dir=custom_example_data, force=True)
    assert len(df) == 2
    assert df.iloc[0]["value"] == 100
    print("SUCCESS: Direct data_dir argument working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_load_with_direct_snapshot_dir_argument():
    """Test that load() accepts snapshot_dir as direct argument."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    custom_example_snapshots = tmp_path / "custom_example_snapshots"
    custom_example_snapshots.mkdir()
    
    import provolone
    
    # Create snapshot with direct snapshot_dir argument (points to dataset's snapshot directory)
    provolone.freeze("example", snapshot="test_direct", snapshot_dir=custom_example_snapshots)
    # With dataset-specific path, snapshot is stored at snapshot_dir/label
    assert (custom_example_snapshots / "test_direct").exists()
    assert not (custom_example_snapshots / "example").exists()
    
    # Load from snapshot with direct snapshot_dir argument
    df = provolone.load("example", snapshot="test_direct", snapshot_dir=custom_example_snapshots)
    assert len(df) == 3  # fallback data
    print("SUCCESS: Direct snapshot_dir argument working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_freeze_with_direct_arguments():
    """Test that freeze() accepts data_dir and snapshot_dir as direct arguments."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    custom_example_data = tmp_path / "custom_example_data"
    custom_example_snapshots = tmp_path / "custom_example_snapshots"
    
    for p in [custom_example_data, custom_example_snapshots]:
        p.mkdir()
    
    # Create test data file directly in dataset directory
    (custom_example_data / "example.csv").write_text("date,value\\n2022-01-01,999\\n")
    
    import provolone
    
    # Freeze with direct arguments (pointing to dataset directories)
    result = provolone.freeze(
        "example", 
        snapshot="direct_test", 
        data_dir=custom_example_data,
        snapshot_dir=custom_example_snapshots
    )
    
    # With dataset-specific path, snapshot is at snapshot_dir/label
    assert (custom_example_snapshots / "direct_test").exists()
    
    # Load and verify it used the custom data_dir
    df = provolone.load("example", snapshot="direct_test", snapshot_dir=custom_example_snapshots)
    assert len(df) == 1
    assert df.iloc[0]["value"] == 999
    print("SUCCESS: freeze() with direct arguments working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_load_with_metadata_direct_arguments():
    """Test that load_with_metadata() accepts direct arguments."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    custom_snapshots = tmp_path / "custom"
    custom_snapshots.mkdir()
    
    import provolone
    
    # Create snapshot with direct argument
    provolone.freeze("example", snapshot="meta_direct", snapshot_dir=custom_snapshots)
    
    # Load with metadata using direct argument
    df, meta = provolone.load_with_metadata("example", snapshot="meta_direct", snapshot_dir=custom_snapshots)
    
    assert len(df) == 3
    assert meta["cache"] == "snapshot-hit"
    print("SUCCESS: load_with_metadata with direct arguments working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_fallback_to_params():
    """Test that the API falls back to params if direct arguments not provided."""
    test_code = '''
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    
    custom_snapshots = tmp_path / "custom"
    custom_snapshots.mkdir()
    
    import provolone
    
    # Create snapshot using params (old style)
    provolone.freeze("example", snapshot="params_test", snapshot_dir=str(custom_snapshots))
    
    # Load using params (old style)
    df = provolone.load("example", snapshot="params_test", snapshot_dir=str(custom_snapshots))
    assert len(df) == 3
    print("SUCCESS: Fallback to params working")
'''
    
    output = run_isolated_test(test_code)
    assert "SUCCESS" in output


def test_cli_build_with_direct_snapshot_dir(tmp_path):
    """Test CLI build command with --snapshot-dir option."""
    custom_example_snapshots = tmp_path / "custom_example_snapshots"
    custom_example_snapshots.mkdir()
    
    # Create a snapshot first
    result = subprocess.run(
        [
            sys.executable, "-m", "provolone.cli",
            "freeze", "example",
            "--label", "cli_test",
            "--snapshot-dir", str(custom_example_snapshots)
        ],
        capture_output=True,
        text=True,
        env={**subprocess.os.environ, "PROVOLONE_SNAPSHOTS_ROOT": str(tmp_path / "global")}
    )
    assert result.returncode == 0
    # With dataset-specific path, snapshot is at snapshot_dir/label
    assert (custom_example_snapshots / "cli_test").exists()
    
    # Now build from that snapshot using --snapshot-dir
    result = subprocess.run(
        [
            sys.executable, "-m", "provolone.cli",
            "build", "example",
            "--snapshot", "cli_test",
            "--snapshot-dir", str(custom_example_snapshots)
        ],
        capture_output=True,
        text=True,
        env={**subprocess.os.environ, "PROVOLONE_SNAPSHOTS_ROOT": str(tmp_path / "global")}
    )
    assert result.returncode == 0
    assert "built:" in result.stdout


def test_cli_freeze_with_direct_options(tmp_path):
    """Test CLI freeze command with --data-dir and --snapshot-dir options."""
    custom_example_data = tmp_path / "custom_example_data"
    custom_example_snapshots = tmp_path / "custom_example_snapshots"
    
    for p in [custom_example_data, custom_example_snapshots]:
        p.mkdir()
    
    # Create test data directly in dataset directory (no example/ subdirectory)
    (custom_example_data / "example.csv").write_text("date,value\n2023-01-01,777\n")
    
    # Freeze with custom paths
    result = subprocess.run(
        [
            sys.executable, "-m", "provolone.cli",
            "freeze", "example",
            "--label", "cli_direct",
            "--data-dir", str(custom_example_data),
            "--snapshot-dir", str(custom_example_snapshots)
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "Snapshot created" in result.stdout
    # With dataset-specific path, snapshot is at snapshot_dir/label
    assert (custom_example_snapshots / "cli_direct").exists()
