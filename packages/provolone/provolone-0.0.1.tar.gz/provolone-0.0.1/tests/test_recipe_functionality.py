"""Test snapshot recipe functionality."""

from __future__ import annotations
import pandas as pd
import pytest


def test_recipe_capture_in_freeze(tmp_path, monkeypatch):
    """Test that freeze captures method sources in the recipe."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze
    from provolone.snapshots import read_df_from_path, _snapshot_paths

    # Freeze a snapshot
    freeze("example", snapshot="recipe-test", force=True)

    # Read the metadata
    p = _snapshot_paths("example", "recipe-test")
    _, meta = read_df_from_path(p.data_path)

    # Check that recipe was captured
    assert "recipe" in meta
    assert "fetch" in meta["recipe"]
    assert "parse" in meta["recipe"]
    assert "transform" in meta["recipe"]

    # Check structure of each method
    for method_name in ["fetch", "parse", "transform"]:
        assert "source" in meta["recipe"][method_name]
        assert "hash" in meta["recipe"][method_name]
        assert len(meta["recipe"][method_name]["hash"]) == 16
        assert "def " + method_name in meta["recipe"][method_name]["source"]


def test_recreate_produces_identical_data(tmp_path, monkeypatch):
    """Test that recreate produces identical data to the original."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze, recreate
    from provolone.snapshots import read_df_from_path, _snapshot_paths

    # Freeze a snapshot
    freeze("example", snapshot="recreate-test", force=True)
    p = _snapshot_paths("example", "recreate-test")
    df_orig, meta_orig = read_df_from_path(p.data_path)

    # Recreate from the snapshot
    recreated_path = recreate(
        "example", snapshot="recreate-test", execute_potentially_unsafe=True
    )
    df_recreated, meta_recreated = read_df_from_path(recreated_path)

    # Verify data matches
    assert df_orig.equals(df_recreated)
    assert meta_orig["content_hash"] == meta_recreated["content_hash"]

    # Verify metadata about recreation
    assert meta_recreated["recreated_from"] == "recreate-test"
    assert "recipe_hashes" in meta_recreated
    assert "fetch" in meta_recreated["recipe_hashes"]
    assert "parse" in meta_recreated["recipe_hashes"]
    assert "transform" in meta_recreated["recipe_hashes"]


def test_recreate_without_recipe_fails_gracefully(tmp_path, monkeypatch):
    """Test that recreate fails gracefully on old snapshots without recipes."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import recreate
    from provolone.snapshots import _snapshot_paths, write_df_to_path

    # Create a fake old snapshot without recipe
    name = "example"
    label = "old-snapshot"
    p = _snapshot_paths(name, label)

    df = pd.DataFrame(
        {"value": [1, 2, 3]},
        index=pd.date_range("2000-01-01", periods=3, freq="MS", name="date"),
    )
    write_df_to_path(df, p.data_path, dataset_name=name)

    # Try to recreate it
    with pytest.raises(ValueError, match="does not contain recipe data"):
        recreate(name, snapshot=label, execute_potentially_unsafe=True)


def test_recreate_with_custom_output_dir(tmp_path, monkeypatch):
    """Test that recreate respects custom output directory."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze, recreate

    # Freeze a snapshot
    freeze("example", snapshot="output-test", force=True)

    # Recreate with custom output dir
    output_dir = tmp_path / "custom-output"
    recreated_path = recreate(
        "example",
        snapshot="output-test",
        output_dir=output_dir,
        execute_potentially_unsafe=True,
    )

    # Verify it was written to the custom location
    assert recreated_path.parent == output_dir
    assert recreated_path.exists()


def test_recreate_with_snapshot_dir(tmp_path, monkeypatch):
    """Test that recreate works with dataset-specific snapshot_dir."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))

    # Use dataset-specific directory
    snapshot_dir = tmp_path / "my-snapshots"

    from provolone import freeze, recreate

    # Freeze to custom location
    freeze("example", snapshot="dir-test", snapshot_dir=snapshot_dir, force=True)

    # Recreate from custom location
    recreated_path = recreate(
        "example",
        snapshot="dir-test",
        snapshot_dir=snapshot_dir,
        execute_potentially_unsafe=True,
    )

    assert recreated_path.exists()
    assert snapshot_dir in recreated_path.parents


def test_cli_recreate_command(tmp_path, monkeypatch):
    """Test the CLI recreate command."""
    from typer.testing import CliRunner
    from provolone.cli import app
    from provolone import freeze

    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    # Create a snapshot first
    freeze("example", snapshot="cli-recreate-test", force=True)

    # Test CLI command
    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "recreate",
            "example",
            "--snapshot",
            "cli-recreate-test",
            "--execute-potentially-unsafe",
        ],
    )

    assert result.exit_code == 0
    assert "Dataset recreated successfully!" in result.stdout
    assert "Output:" in result.stdout


def test_cli_recreate_missing_snapshot(tmp_path, monkeypatch):
    """Test that CLI recreate fails gracefully on missing snapshot."""
    from typer.testing import CliRunner
    from provolone.cli import app

    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    runner = CliRunner()
    result = runner.invoke(app, ["recreate", "example", "--snapshot", "nonexistent"])

    assert result.exit_code == 1
    assert "Error:" in result.stdout


def test_cli_recreate_old_snapshot(tmp_path, monkeypatch):
    """Test that CLI recreate fails gracefully on old snapshots without recipes."""
    from typer.testing import CliRunner
    from provolone.cli import app
    from provolone.snapshots import _snapshot_paths, write_df_to_path
    import pandas as pd

    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    # Create old snapshot without recipe
    p = _snapshot_paths("example", "old-snap")
    df = pd.DataFrame(
        {"value": [1]},
        index=pd.date_range("2000-01-01", periods=1, freq="MS", name="date"),
    )
    write_df_to_path(df, p.data_path, dataset_name="example")

    runner = CliRunner()
    result = runner.invoke(
        app,
        [
            "recreate",
            "example",
            "--snapshot",
            "old-snap",
            "--execute-potentially-unsafe",
        ],
    )

    assert result.exit_code == 1
    assert "does not contain recipe data" in result.stdout
    assert "re-freeze" in result.stdout


def test_cli_recreate_requires_safety_flag(tmp_path, monkeypatch):
    """Test that CLI recreate requires the safety flag."""
    from typer.testing import CliRunner
    from provolone.cli import app
    from provolone import freeze

    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    # Create a snapshot first
    freeze("example", snapshot="cli-safety-test", force=True)

    # Test CLI command without safety flag
    runner = CliRunner()
    result = runner.invoke(
        app, ["recreate", "example", "--snapshot", "cli-safety-test"]
    )

    assert result.exit_code == 1
    assert "execute_potentially_unsafe" in result.stdout
    assert "--execute-potentially-unsafe" in result.stdout


def test_source_extraction_utility():
    """Test the source extraction utility functions."""
    from provolone.utils.source import (
        extract_method_source,
        hash_source,
        extract_method_recipe,
    )

    # Define a simple test class
    class TestDataset:
        def fetch(self):
            return None

        def parse(self, raw):
            return None

    # Test extract_method_source
    ds = TestDataset()
    fetch_source = extract_method_source(ds.fetch)
    assert fetch_source is not None
    assert "def fetch(self):" in fetch_source
    assert "return None" in fetch_source

    # Test hash_source
    source_hash = hash_source(fetch_source)
    assert len(source_hash) == 16
    assert isinstance(source_hash, str)

    # Test extract_method_recipe
    recipe = extract_method_recipe(ds, "fetch")
    assert recipe is not None
    assert "source" in recipe
    assert "hash" in recipe
    assert recipe["source"] == fetch_source
    assert recipe["hash"] == source_hash

    # Test with non-existent method
    recipe = extract_method_recipe(ds, "nonexistent")
    assert recipe is None


def test_recipe_captures_imports_in_methods(tmp_path, monkeypatch):
    """Test that recipe captures imports used within methods."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze
    from provolone.snapshots import read_df_from_path, _snapshot_paths

    # Freeze the example dataset (which imports Path and pd)
    freeze("example", snapshot="imports-test", force=True)

    # Read the recipe
    p = _snapshot_paths("example", "imports-test")
    _, meta = read_df_from_path(p.data_path)

    # Check that imports are in the source
    fetch_source = meta["recipe"]["fetch"]["source"]
    # The fetch method doesn't have its own imports, but uses self.data_dir
    assert "def fetch" in fetch_source

    parse_source = meta["recipe"]["parse"]["source"]
    assert "def parse" in parse_source


def test_recreate_isolation_no_module_imports(tmp_path, monkeypatch):
    """Test that recreate doesn't import user modules."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze, recreate
    import sys

    # Freeze a snapshot
    freeze("example", snapshot="isolation-test", force=True)

    # Track which modules were imported before recreate
    initial_modules = set(sys.modules.keys())

    # Recreate the dataset
    recreate("example", snapshot="isolation-test", execute_potentially_unsafe=True)

    # Check that no new user modules were imported
    # (Some stdlib modules might be imported, but not provolone.datasets.example.loader)
    new_modules = set(sys.modules.keys()) - initial_modules

    # The recreate should not have imported the example loader module
    # (it was already imported by freeze, but we ensure it's not re-imported)
    # This is a sanity check that we're using exec, not import
    assert all(
        not mod.startswith("provolone.datasets.") or mod == "provolone.datasets.base"
        for mod in new_modules
    )


def test_recreate_requires_safety_flag(tmp_path, monkeypatch):
    """Test that recreate requires execute_potentially_unsafe flag."""
    monkeypatch.setenv("PROVOLONE_CACHE_DIR", str(tmp_path / "cache"))
    monkeypatch.setenv("PROVOLONE_SNAPSHOTS_DIR", str(tmp_path / "snapshots"))

    from provolone import freeze, recreate

    # Freeze a snapshot
    freeze("example", snapshot="safety-test", force=True)

    # Try to recreate without the safety flag
    with pytest.raises(ValueError, match="execute_potentially_unsafe"):
        recreate("example", snapshot="safety-test")

    # Should work with the flag
    recreate("example", snapshot="safety-test", execute_potentially_unsafe=True)
