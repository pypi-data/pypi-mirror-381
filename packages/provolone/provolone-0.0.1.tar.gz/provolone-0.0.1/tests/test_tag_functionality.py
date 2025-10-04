"""Test tag functionality for file metadata."""

from __future__ import annotations
import json
import tempfile
from pathlib import Path

from provolone import tag, load_with_metadata
from provolone.cli import app
from typer.testing import CliRunner


def test_tag_function_basic():
    """Test basic tag function functionality."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")
        f.flush()

        try:
            # Tag the file
            meta_path = tag(
                f.name,
                raw_file_url="https://example.com/data.csv",
                raw_file_notes="Test data file",
            )

            # Check that metadata file was created
            assert meta_path.exists()
            assert meta_path.name == Path(f.name).with_suffix(".meta.json").name

            # Check metadata content
            with open(meta_path) as meta_file:
                metadata = json.load(meta_file)

            assert metadata["raw_file_url"] == "https://example.com/data.csv"
            assert metadata["raw_file_notes"] == "Test data file"
            assert metadata["raw_file_name"] == Path(f.name).name
            assert metadata["raw_file_exists"] is True
            assert metadata["raw_file_type"] == "csv"
            assert metadata["raw_file_size"] > 0

        finally:
            # Cleanup
            Path(f.name).unlink(missing_ok=True)
            meta_path.unlink(missing_ok=True)


def test_tag_function_no_extension():
    """Test tag function with file that has no extension."""
    with tempfile.NamedTemporaryFile(mode="w", suffix="", delete=False) as f:
        f.write("test content")
        f.flush()

        try:
            meta_path = tag(f.name, raw_file_url="test://source")

            assert meta_path.exists()
            assert meta_path.suffix == ".json"
            assert "meta.json" in meta_path.name

        finally:
            Path(f.name).unlink(missing_ok=True)
            meta_path.unlink(missing_ok=True)


def test_tag_function_additional_metadata():
    """Test tag function with additional metadata fields."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("test content")
        f.flush()

        try:
            meta_path = tag(
                f.name,
                raw_file_url="test://source",
                custom_field="custom_value",
                another_field=42,
            )

            with open(meta_path) as meta_file:
                metadata = json.load(meta_file)

            assert metadata["raw_file_url"] == "test://source"
            assert metadata["custom_field"] == "custom_value"
            assert metadata["another_field"] == 42

        finally:
            Path(f.name).unlink(missing_ok=True)
            meta_path.unlink(missing_ok=True)


def test_cli_tag_command():
    """Test the CLI tag command."""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n")
        f.flush()

        try:
            # Test CLI tag command
            result = runner.invoke(
                app,
                [
                    "tag",
                    f.name,
                    "--raw_file_url",
                    "https://example.com/cli-test.csv",
                    "--raw_file_notes",
                    "CLI test file",
                ],
            )

            assert result.exit_code == 0
            assert "Metadata file created:" in result.stdout

            # Check that metadata file was created
            expected_meta_path = Path(f.name).with_suffix(".meta.json")
            assert expected_meta_path.exists()

            with open(expected_meta_path) as meta_file:
                metadata = json.load(meta_file)

            assert metadata["raw_file_url"] == "https://example.com/cli-test.csv"
            assert metadata["raw_file_notes"] == "CLI test file"

        finally:
            Path(f.name).unlink(missing_ok=True)
            Path(f.name).with_suffix(".meta.json").unlink(missing_ok=True)


def test_cli_tag_command_minimal():
    """Test the CLI tag command with minimal options."""
    runner = CliRunner()

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("date,value\n2024-01-01,10\n")
        f.flush()

        try:
            # Test CLI tag command with no metadata options
            result = runner.invoke(app, ["tag", f.name])

            assert result.exit_code == 0
            assert "Metadata file created:" in result.stdout

            # Check that metadata file was created
            expected_meta_path = Path(f.name).with_suffix(".meta.json")
            assert expected_meta_path.exists()

            with open(expected_meta_path) as meta_file:
                metadata = json.load(meta_file)

            # Should have basic file metadata even without source/notes
            assert metadata["raw_file_name"] == Path(f.name).name
            assert metadata["raw_file_exists"] is True
            assert "raw_file_url" not in metadata
            assert "raw_file_source" not in metadata
            assert "raw_file_notes" not in metadata

        finally:
            Path(f.name).unlink(missing_ok=True)
            Path(f.name).with_suffix(".meta.json").unlink(missing_ok=True)


def test_sidecar_metadata_integration_with_load(tmp_path):
    """Test that sidecar metadata is used as defaults when loading datasets."""
    # Create example dataset structure
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"

    # Create test CSV data
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")

    # Create sidecar metadata
    meta_path = tag(
        str(csv_file),
        raw_file_url="https://sidecar.com/data.csv",
        raw_file_notes="From sidecar metadata",
    )
    assert meta_path.exists()

    # Load dataset without explicit metadata - should use sidecar defaults
    df, meta = load_with_metadata("example", force=True, data_root=str(tmp_path))

    # Check that sidecar metadata was used (now in raw_files list)
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    assert raw_meta["raw_file_url"] == "https://sidecar.com/data.csv"
    assert raw_meta["raw_file_notes"] == "From sidecar metadata"

    # Check the data loaded correctly
    assert len(df) == 2
    assert "value" in df.columns


def test_sidecar_metadata_override_with_explicit_params(tmp_path):
    """Test that sidecar metadata takes precedence over explicit parameters."""
    # Create example dataset structure
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"

    # Create test CSV data
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")

    # Create sidecar metadata
    tag(
        str(csv_file),
        raw_file_url="https://sidecar.com/data.csv",
        raw_file_notes="From sidecar metadata",
    )

    # Load dataset with params - sidecar should take precedence
    df, meta = load_with_metadata(
        "example",
        force=True,
        data_root=str(tmp_path),
        raw_file_url="https://explicit.com/data.csv",
        raw_file_notes="Explicit metadata",
    )

    # Check that sidecar metadata was used, not params (now in raw_files list)
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    assert raw_meta["raw_file_url"] == "https://sidecar.com/data.csv"
    assert raw_meta["raw_file_notes"] == "From sidecar metadata"


def test_sidecar_metadata_partial_override(tmp_path):
    """Test that params are used only for fields not in sidecar metadata."""
    # Create example dataset structure
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"

    # Create test CSV data
    with open(csv_file, "w") as f:
        f.write("date,value\n2024-01-01,10\n2024-02-01,20\n")

    # Create sidecar metadata with only url (no notes or source)
    tag(
        str(csv_file),
        raw_file_url="https://sidecar.com/data.csv"
    )

    # Load dataset with source provided - sidecar url should be used, param source should be used
    df, meta = load_with_metadata(
        "example",
        force=True,
        data_root=str(tmp_path),
        raw_file_source="Fallback Provider",
        raw_file_notes="Fallback notes"
    )

    # Check that sidecar url was used but param source/notes were used for missing fields
    assert "raw_files" in meta
    assert len(meta["raw_files"]) == 1
    raw_meta = meta["raw_files"][0]
    assert raw_meta["raw_file_url"] == "https://sidecar.com/data.csv"  # from sidecar
    assert raw_meta["raw_file_source"] == "Fallback Provider"  # from param (not in sidecar)
    assert raw_meta["raw_file_notes"] == "Fallback notes"  # from param (not in sidecar)


def test_tag_nonexistent_file():
    """Test tagging a nonexistent file."""
    nonexistent_path = "/tmp/does_not_exist.csv"

    # Should still create metadata file even if source file doesn't exist
    meta_path = tag(
        nonexistent_path,
        raw_file_url="https://future.com/data.csv",
        raw_file_notes="Will be downloaded later",
    )

    try:
        assert meta_path.exists()

        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://future.com/data.csv"
        assert metadata["raw_file_notes"] == "Will be downloaded later"
        assert metadata["raw_file_exists"] is False
        assert "raw_file_size" not in metadata
        assert "raw_file_sha256" not in metadata

    finally:
        meta_path.unlink(missing_ok=True)
