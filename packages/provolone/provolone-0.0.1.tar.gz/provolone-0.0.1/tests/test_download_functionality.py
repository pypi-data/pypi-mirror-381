"""Test download functionality for file downloads with automatic tagging."""

from __future__ import annotations
import json
from unittest.mock import patch
import pytest

from provolone import download
from provolone.cli import app
from typer.testing import CliRunner


def test_download_basic(tmp_path, monkeypatch):
    """Test basic download functionality."""
    # Change to temp directory
    monkeypatch.chdir(tmp_path)

    # Mock urllib.request.urlretrieve
    def mock_urlretrieve(url, filename):
        # Create a fake file
        with open(filename, "w") as f:
            f.write("test,data\n1,2\n3,4\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        # Download to current directory (default)
        file_path = download("https://example.com/data.csv")

        # Check file was created
        assert file_path.exists()
        assert file_path.name == "data.csv"

        # Check metadata file was created
        meta_path = file_path.with_suffix(".meta.json")
        assert meta_path.exists()

        # Check metadata content
        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://example.com/data.csv"
        assert metadata["raw_file_exists"] is True
        assert "raw_file_notes" not in metadata


def test_download_with_destination(tmp_path):
    """Test download with explicit destination path."""
    dest = tmp_path / "subdir" / "my_data.csv"

    # Mock urllib.request.urlretrieve
    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n1,2\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download("https://example.com/data.csv", destination=dest)

        # Check file was created at specified location
        assert file_path == dest
        assert file_path.exists()
        assert file_path.parent.exists()

        # Check metadata
        meta_path = file_path.with_suffix(".meta.json")
        assert meta_path.exists()

        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://example.com/data.csv"
        assert metadata["raw_file_name"] == "my_data.csv"


def test_download_with_notes(tmp_path, monkeypatch):
    """Test download with notes parameter."""
    monkeypatch.chdir(tmp_path)

    # Mock urllib.request.urlretrieve
    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n1,2\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download(
            "https://example.com/data.csv", notes="Downloaded for testing purposes"
        )

        # Check metadata includes notes
        meta_path = file_path.with_suffix(".meta.json")
        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://example.com/data.csv"
        assert metadata["raw_file_notes"] == "Downloaded for testing purposes"


def test_download_with_destination_and_notes(tmp_path):
    """Test download with both destination and notes."""
    dest = tmp_path / "my_data.csv"

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n1,2\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download(
            "https://example.com/production/data.csv",
            destination=dest,
            notes="Production data snapshot 2024-12-27",
        )

        assert file_path == dest
        assert file_path.exists()

        meta_path = file_path.with_suffix(".meta.json")
        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://example.com/production/data.csv"
        assert metadata["raw_file_notes"] == "Production data snapshot 2024-12-27"


def test_download_creates_parent_directory(tmp_path):
    """Test that download creates parent directories if they don't exist."""
    dest = tmp_path / "deeply" / "nested" / "path" / "data.csv"

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download("https://example.com/data.csv", destination=dest)

        assert file_path.exists()
        assert file_path.parent.exists()
        assert (tmp_path / "deeply" / "nested" / "path").exists()


def test_download_no_filename_in_url():
    """Test error handling when URL has no filename."""
    with patch("urllib.request.urlretrieve"):
        with pytest.raises(ValueError, match="Could not determine filename from URL"):
            download("https://example.com/")


def test_download_network_error(tmp_path, monkeypatch):
    """Test error handling when download fails."""
    monkeypatch.chdir(tmp_path)

    def mock_urlretrieve_error(url, filename):
        raise Exception("Network error")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve_error):
        with pytest.raises(RuntimeError, match="Failed to download"):
            download("https://example.com/data.csv")


def test_download_with_query_params(tmp_path, monkeypatch):
    """Test download with URL that has query parameters."""
    monkeypatch.chdir(tmp_path)

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download("https://example.com/data.csv?version=2&format=csv")

        assert file_path.exists()
        assert file_path.name == "data.csv"

        # Check metadata records full URL
        meta_path = file_path.with_suffix(".meta.json")
        with open(meta_path) as f:
            metadata = json.load(f)

        assert (
            metadata["raw_file_url"]
            == "https://example.com/data.csv?version=2&format=csv"
        )


def test_cli_download_command(tmp_path, monkeypatch):
    """Test the CLI download command."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n1,2\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        result = runner.invoke(app, ["download", "https://example.com/test.csv"])

        assert result.exit_code == 0
        assert "Downloaded to:" in result.stdout
        assert "Metadata file created:" in result.stdout

        # Check file and metadata were created
        assert (tmp_path / "test.csv").exists()
        assert (tmp_path / "test.meta.json").exists()


def test_cli_download_with_destination(tmp_path, monkeypatch):
    """Test CLI download with destination option."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    dest = tmp_path / "my_file.csv"

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        result = runner.invoke(
            app,
            ["download", "https://example.com/test.csv", "--destination", str(dest)],
        )

        assert result.exit_code == 0
        assert dest.exists()
        assert dest.with_suffix(".meta.json").exists()


def test_cli_download_with_destination_short_option(tmp_path, monkeypatch):
    """Test CLI download with -d short option."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    dest = tmp_path / "my_file.csv"

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        result = runner.invoke(
            app, ["download", "https://example.com/test.csv", "-d", str(dest)]
        )

        assert result.exit_code == 0
        assert dest.exists()


def test_cli_download_with_notes(tmp_path, monkeypatch):
    """Test CLI download with notes option."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        result = runner.invoke(
            app,
            ["download", "https://example.com/test.csv", "--notes", "Test download"],
        )

        assert result.exit_code == 0

        # Check metadata includes notes
        meta_path = tmp_path / "test.meta.json"
        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_notes"] == "Test download"


def test_cli_download_with_all_options(tmp_path, monkeypatch):
    """Test CLI download with all options."""
    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    dest = tmp_path / "custom.csv"

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        result = runner.invoke(
            app,
            [
                "download",
                "https://example.com/test.csv",
                "--destination",
                str(dest),
                "--notes",
                "Production snapshot",
            ],
        )

        assert result.exit_code == 0
        assert dest.exists()

        meta_path = dest.with_suffix(".meta.json")
        with open(meta_path) as f:
            metadata = json.load(f)

        assert metadata["raw_file_url"] == "https://example.com/test.csv"
        assert metadata["raw_file_notes"] == "Production snapshot"


def test_download_different_file_types(tmp_path, monkeypatch):
    """Test download with various file extensions."""
    monkeypatch.chdir(tmp_path)

    def mock_urlretrieve(url, filename):
        with open(filename, "wb") as f:
            f.write(b"test content")

    file_types = [
        "data.csv",
        "data.xlsx",
        "data.json",
        "data.txt",
        "data.parquet",
    ]

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        for filename in file_types:
            url = f"https://example.com/{filename}"
            file_path = download(url)

            assert file_path.exists()
            assert file_path.name == filename
            assert file_path.with_suffix(".meta.json").exists()


def test_download_metadata_has_all_expected_fields(tmp_path, monkeypatch):
    """Test that download creates metadata with all expected fields."""
    monkeypatch.chdir(tmp_path)

    def mock_urlretrieve(url, filename):
        with open(filename, "w") as f:
            f.write("test,data\n1,2,3\n4,5,6\n")

    with patch("urllib.request.urlretrieve", side_effect=mock_urlretrieve):
        file_path = download("https://example.com/data.csv", notes="Test metadata")

        meta_path = file_path.with_suffix(".meta.json")
        with open(meta_path) as f:
            metadata = json.load(f)

        # Check essential fields are present
        assert "raw_file_url" in metadata
        assert "raw_file_notes" in metadata
        assert "raw_file_path" in metadata
        assert "raw_file_name" in metadata
        assert "raw_file_exists" in metadata
        assert "raw_file_size" in metadata
        assert "raw_file_mtime" in metadata
        assert "raw_file_sha256" in metadata
        assert "raw_file_type" in metadata

        # Check values
        assert metadata["raw_file_url"] == "https://example.com/data.csv"
        assert metadata["raw_file_notes"] == "Test metadata"
        assert metadata["raw_file_exists"] is True
        assert metadata["raw_file_size"] > 0
        assert metadata["raw_file_type"] == "csv"
