"""Test that directories are created lazily, not on import."""

from __future__ import annotations
import subprocess
import sys


def test_directories_not_created_on_import():
    """Verify that importing provolone does NOT create directories."""
    test_code = """
import os
import sys
import tempfile
from pathlib import Path

# Create temporary directories for testing
with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    test_data_root = tmp_path / "test_data"
    test_cache_dir = tmp_path / "test_cache"
    test_snapshots_root = tmp_path / "test_snapshots"
    
    # Set environment variables to use test directories
    os.environ["PROVOLONE_DATA_ROOT"] = str(test_data_root)
    os.environ["PROVOLONE_CACHE_DIR"] = str(test_cache_dir)
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(test_snapshots_root)
    
    # Import provolone - this should NOT create any directories
    import provolone
    from provolone.config import cfg
    
    # Verify directories don't exist yet
    assert not test_data_root.exists(), f"data_root should not exist yet but found: {test_data_root}"
    assert not test_cache_dir.exists(), f"cache_dir should not exist yet but found: {test_cache_dir}"
    assert not test_snapshots_root.exists(), f"snapshots_root should not exist yet but found: {test_snapshots_root}"
    
    print("SUCCESS: No directories created on import")
"""

    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True,
    )

    assert (
        result.returncode == 0
    ), f"Test failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"
    assert "SUCCESS" in result.stdout


def test_directories_created_when_used():
    """Verify that directories ARE created when actually needed."""
    test_code = """
import os
import sys
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    test_cache_dir = tmp_path / "test_cache"
    test_snapshots_root = tmp_path / "test_snapshots"
    
    # Set environment variables
    os.environ["PROVOLONE_CACHE_DIR"] = str(test_cache_dir)
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(test_snapshots_root)
    
    # Import provolone
    import provolone
    from provolone.config import cfg
    
    # Verify directories don't exist yet
    assert not test_cache_dir.exists(), "cache_dir should not exist yet"
    assert not test_snapshots_root.exists(), "snapshots_root should not exist yet"
    
    # Now use the example dataset - this should create directories
    df = provolone.load("example")
    
    # Verify the snapshot directory structure was created
    # The _default cache should be created at snapshots_root/example/_default/data.parquet
    expected_cache_path = test_snapshots_root / "example" / "_default"
    assert expected_cache_path.exists(), f"Cache directory should exist at {expected_cache_path}"
    
    print("SUCCESS: Directories created when used")
"""

    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True,
    )

    assert (
        result.returncode == 0
    ), f"Test failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"
    assert "SUCCESS" in result.stdout


def test_snapshot_creation_makes_directories():
    """Verify that creating a snapshot creates necessary directories."""
    test_code = """
import os
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)
    test_snapshots_root = tmp_path / "test_snapshots"
    
    os.environ["PROVOLONE_SNAPSHOTS_ROOT"] = str(test_snapshots_root)
    
    import provolone
    
    # Verify directory doesn't exist yet
    assert not test_snapshots_root.exists(), "snapshots_root should not exist yet"
    
    # Create a snapshot
    snapshot_path = provolone.freeze("example", snapshot="test_snapshot")
    
    # Verify the snapshot directory was created
    expected_path = test_snapshots_root / "example" / "test_snapshot"
    assert expected_path.exists(), f"Snapshot directory should exist at {expected_path}"
    assert snapshot_path == expected_path, f"Snapshot path mismatch: {snapshot_path} != {expected_path}"
    
    print("SUCCESS: Snapshot directory created")
"""

    result = subprocess.run(
        [sys.executable, "-c", test_code],
        capture_output=True,
        text=True,
    )

    assert (
        result.returncode == 0
    ), f"Test failed:\nstdout: {result.stdout}\nstderr: {result.stderr}"
    assert "SUCCESS" in result.stdout
