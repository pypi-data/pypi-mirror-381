"""Test CLI commands including build and info."""
from __future__ import annotations
from typer.testing import CliRunner
from provolone.cli import app

runner = CliRunner()


def test_cli_build_command(tmp_path, monkeypatch):
    """Test the build command (renamed from load)."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Run build command
    result = runner.invoke(app, ["build", "example"])
    
    assert result.exit_code == 0
    assert "example built" in result.stdout
    assert "shape=" in result.stdout


def test_cli_build_command_with_head(tmp_path, monkeypatch):
    """Test the build command with --head option."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Run build command with head
    result = runner.invoke(app, ["build", "example", "--head", "2"])
    
    assert result.exit_code == 0
    # Should show actual data rows
    assert "date" in result.stdout or "value" in result.stdout


def test_cli_build_command_with_params(tmp_path, monkeypatch):
    """Test the build command with parameters."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Run build command with params
    result = runner.invoke(app, ["build", "example", "--params", "test_param=value"])
    
    assert result.exit_code == 0
    assert "example built" in result.stdout


def test_cli_info_command(tmp_path, monkeypatch):
    """Test the info command shows metadata."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # First build the dataset
    result = runner.invoke(app, ["build", "example"])
    assert result.exit_code == 0
    
    # Now get info
    result = runner.invoke(app, ["info", "example"])
    
    assert result.exit_code == 0
    assert "Dataset: example" in result.stdout
    assert "Shape:" in result.stdout
    assert "rows" in result.stdout
    assert "columns" in result.stdout


def test_cli_info_command_with_snapshot(tmp_path, monkeypatch):
    """Test the info command with a snapshot."""
    import uuid
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # First build the dataset
    result = runner.invoke(app, ["build", "example"])
    assert result.exit_code == 0
    
    # Create a snapshot with unique name
    snap_name = f"test-snap-{uuid.uuid4().hex[:8]}"
    result = runner.invoke(app, ["freeze", "example", "--label", snap_name])
    assert result.exit_code == 0
    
    # Now get info for the snapshot
    result = runner.invoke(app, ["info", "example", "--snapshot", snap_name])
    
    assert result.exit_code == 0
    assert "Dataset: example" in result.stdout
    assert f"Label: {snap_name}" in result.stdout
    assert "Shape:" in result.stdout


def test_cli_info_command_nonexistent_dataset(tmp_path, monkeypatch):
    """Test the info command with a nonexistent dataset."""
    # Set up temp cache directory with unique name
    unique_name = "nonexistent_test_dataset_unique_12345"
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Try to get info for a dataset that doesn't exist
    result = runner.invoke(app, ["info", unique_name])
    
    # Should either exit with error or show not found message
    assert result.exit_code == 1 or "not found" in result.stdout.lower() or "error" in result.stdout.lower()


def test_cli_info_command_nonexistent_snapshot(tmp_path, monkeypatch):
    """Test the info command with a nonexistent snapshot."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Try to get info for a snapshot that doesn't exist
    result = runner.invoke(app, ["info", "example", "--snapshot", "nonexistent"])
    
    assert result.exit_code == 1
    assert "not found" in result.stdout or "Error" in result.stdout


def test_cli_info_shows_index_info(tmp_path, monkeypatch):
    """Test that info command shows index information."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Build the dataset
    result = runner.invoke(app, ["build", "example"])
    assert result.exit_code == 0
    
    # Get info
    result = runner.invoke(app, ["info", "example"])
    
    assert result.exit_code == 0
    # Should show index information
    assert "Index:" in result.stdout
    assert "Names:" in result.stdout or "Types:" in result.stdout


def test_cli_info_shows_file_info(tmp_path, monkeypatch):
    """Test that info command shows file information."""
    # Set up temp cache directory
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))
    
    # Build the dataset
    result = runner.invoke(app, ["build", "example"])
    assert result.exit_code == 0
    
    # Get info
    result = runner.invoke(app, ["info", "example"])
    
    assert result.exit_code == 0
    # Should show file information
    assert "File Info:" in result.stdout or "Format:" in result.stdout
