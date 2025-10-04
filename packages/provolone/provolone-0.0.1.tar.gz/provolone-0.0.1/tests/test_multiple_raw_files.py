"""Test multiple raw file metadata recording functionality."""
from __future__ import annotations
import csv
from pathlib import Path
import pandas as pd
import pytest

from provolone import load_with_metadata, freeze
from provolone.datasets import register
from provolone.datasets.base import BaseDataset
from provolone.utils.hash import hash_file


@register("multi_file_test")
class MultiFileDataset(BaseDataset):
    """Test dataset that uses multiple raw files."""
    
    name = "multi_file_test"
    frequency = "m"
    
    def fetch(self):
        """Return multiple file paths."""
        file1 = self.data_dir / "file1.csv"
        file2 = self.data_dir / "file2.csv"
        
        # Return list of files if they exist, otherwise None
        if file1.exists() and file2.exists():
            return [file1, file2]
        return None
    
    def parse(self, raw) -> pd.DataFrame:
        """Parse multiple files and combine them."""
        if raw is None or not isinstance(raw, list):
            # Fallback minimal DF
            df = pd.DataFrame({
                "date": pd.date_range("2000-01-01", periods=2, freq="MS"),
                "value": [1.0, 2.0],
            })
            return df.set_index("date")
        
        # Read both files and concatenate
        dfs = []
        for file_path in raw:
            df = pd.read_csv(file_path, parse_dates=["date"])
            dfs.append(df.set_index("date"))
        
        return pd.concat(dfs)


def test_multiple_files_metadata(tmp_path):
    """Test that metadata is recorded for multiple raw files using sidecar metadata."""
    from provolone import tag
    
    # Create test directory structure
    dataset_dir = tmp_path / "multi_file_test"
    dataset_dir.mkdir()
    
    # Create first CSV file
    file1 = dataset_dir / "file1.csv"
    with open(file1, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
        writer.writerow(['2024-02-01', '20.0'])
    
    # Create second CSV file
    file2 = dataset_dir / "file2.csv"
    with open(file2, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-03-01', '30.0'])
        writer.writerow(['2024-04-01', '40.0'])
    
    # Tag each file with its own metadata
    tag(
        str(file1),
        raw_file_url="https://example.com/file1.csv",
        raw_file_source="Provider A",
        raw_file_notes="First file with Jan-Feb data"
    )
    tag(
        str(file2),
        raw_file_url="https://example.com/file2.csv",
        raw_file_source="Provider B",
        raw_file_notes="Second file with Mar-Apr data"
    )
    
    # Load dataset - metadata should come from sidecar files
    df, meta = load_with_metadata(
        "multi_file_test",
        force=True,
        data_dir=str(dataset_dir)
    )
    
    # Check that raw_files is a list
    assert 'raw_files' in meta
    assert isinstance(meta['raw_files'], list)
    assert len(meta['raw_files']) == 2
    
    # Check first file metadata
    file1_meta = meta['raw_files'][0]
    assert file1_meta['raw_file_path'] == str(file1.absolute())
    assert file1_meta['raw_file_name'] == 'file1.csv'
    assert file1_meta['raw_file_exists'] is True
    assert file1_meta['raw_file_type'] == 'csv'
    assert file1_meta['raw_file_size'] > 0
    assert len(file1_meta['raw_file_sha256']) == 64
    assert file1_meta['raw_file_url'] == "https://example.com/file1.csv"
    assert file1_meta['raw_file_source'] == "Provider A"
    assert file1_meta['raw_file_notes'] == "First file with Jan-Feb data"
    
    # Check second file metadata
    file2_meta = meta['raw_files'][1]
    assert file2_meta['raw_file_path'] == str(file2.absolute())
    assert file2_meta['raw_file_name'] == 'file2.csv'
    assert file2_meta['raw_file_exists'] is True
    assert file2_meta['raw_file_type'] == 'csv'
    assert file2_meta['raw_file_size'] > 0
    assert len(file2_meta['raw_file_sha256']) == 64
    assert file2_meta['raw_file_url'] == "https://example.com/file2.csv"
    assert file2_meta['raw_file_source'] == "Provider B"
    assert file2_meta['raw_file_notes'] == "Second file with Mar-Apr data"
    
    # Verify hashes match actual file content
    expected_hash1 = hash_file(file1, truncate=False)
    assert file1_meta['raw_file_sha256'] == expected_hash1
    
    expected_hash2 = hash_file(file2, truncate=False)
    assert file2_meta['raw_file_sha256'] == expected_hash2
    
    # Check that the DataFrame was loaded correctly (4 rows total)
    assert len(df) == 4
    assert list(df.columns) == ['value']
    assert df.index.name == 'date'


def test_multiple_files_with_default_metadata(tmp_path):
    """Test that non-indexed metadata applies to all files as default."""
    # Create test directory structure
    dataset_dir = tmp_path / "multi_file_test"
    dataset_dir.mkdir()
    
    # Create two CSV files
    file1 = dataset_dir / "file1.csv"
    with open(file1, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
    
    file2 = dataset_dir / "file2.csv"
    with open(file2, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-02-01', '20.0'])
    
    # Load with default metadata (no indexes)
    df, meta = load_with_metadata(
        "multi_file_test",
        force=True,
        data_dir=str(dataset_dir),
        raw_file_source="Common Provider"
    )
    
    # Check that both files got the default source
    assert 'raw_files' in meta
    assert len(meta['raw_files']) == 2
    assert meta['raw_files'][0]['raw_file_source'] == "Common Provider"
    assert meta['raw_files'][1]['raw_file_source'] == "Common Provider"


def test_single_file_backward_compatibility(tmp_path):
    """Test that single file datasets still work and produce raw_files list."""
    # Create example CSV file
    example_dir = tmp_path / "example"
    example_dir.mkdir()
    csv_file = example_dir / "example.csv"
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
    
    # Load dataset with single file
    df, meta = load_with_metadata(
        "example",
        force=True,
        data_dir=str(example_dir),
        raw_file_url="https://example.com/data.csv"
    )
    
    # Should have raw_files as a list with one element
    assert 'raw_files' in meta
    assert isinstance(meta['raw_files'], list)
    assert len(meta['raw_files']) == 1
    
    # Check the single file metadata
    file_meta = meta['raw_files'][0]
    assert file_meta['raw_file_path'] == str(csv_file.absolute())
    assert file_meta['raw_file_name'] == 'example.csv'
    assert file_meta['raw_file_url'] == "https://example.com/data.csv"


def test_multiple_files_in_snapshot(tmp_path):
    """Test that multiple file metadata is preserved in snapshots using sidecar metadata."""
    from provolone import tag
    
    # Create test directory structure
    dataset_dir = tmp_path / "multi_file_test"
    dataset_dir.mkdir()
    
    file1 = dataset_dir / "file1.csv"
    with open(file1, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '100.0'])
    
    file2 = dataset_dir / "file2.csv"
    with open(file2, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-02-01', '200.0'])
    
    # Tag files with metadata
    tag(
        str(file1),
        raw_file_url="https://example.com/snap1.csv"
    )
    tag(
        str(file2),
        raw_file_url="https://example.com/snap2.csv"
    )
    
    snapshot_dir = tmp_path / "snapshots"
    
    # Create snapshot - metadata should come from sidecar files
    # Using dataset-specific snapshot_dir (new API)
    snapshot_path = freeze(
        "multi_file_test",
        snapshot="test-multi",
        data_dir=str(dataset_dir),
        snapshot_dir=str(snapshot_dir)
    )
    
    # Read snapshot using the same dataset-specific snapshot_dir
    from provolone import load_with_metadata
    df, meta = load_with_metadata("multi_file_test", snapshot="test-multi", snapshot_dir=str(snapshot_dir))
    
    assert 'raw_files' in meta
    assert len(meta['raw_files']) == 2
    assert meta['raw_files'][0]['raw_file_url'] == "https://example.com/snap1.csv"
    assert meta['raw_files'][1]['raw_file_url'] == "https://example.com/snap2.csv"


def test_multiple_files_cached(tmp_path):
    """Test that multiple file metadata persists in cache using sidecar metadata."""
    from provolone import tag
    
    # Create test directory structure
    dataset_dir = tmp_path / "multi_file_test"
    dataset_dir.mkdir()
    
    file1 = dataset_dir / "file1.csv"
    with open(file1, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-01-01', '10.0'])
    
    file2 = dataset_dir / "file2.csv"
    with open(file2, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'value'])
        writer.writerow(['2024-02-01', '20.0'])
    
    # Tag files with metadata
    tag(
        str(file1),
        raw_file_url="https://test.com/f1.csv"
    )
    tag(
        str(file2),
        raw_file_url="https://test.com/f2.csv"
    )
    
    cache_dir = tmp_path / "cache"
    
    # First load - should compute fresh
    df1, meta1 = load_with_metadata(
        "multi_file_test",
        force=True,
        data_dir=str(dataset_dir),
        snapshot_dir=str(cache_dir)
    )
    assert meta1['cache'] == 'miss'
    assert len(meta1['raw_files']) == 2
    
    # Second load - should hit cache
    df2, meta2 = load_with_metadata(
        "multi_file_test",
        data_dir=str(dataset_dir),
        snapshot_dir=str(cache_dir)
    )
    assert meta2['cache'] == 'hit'
    assert len(meta2['raw_files']) == 2
    assert meta2['raw_files'][0]['raw_file_url'] == "https://test.com/f1.csv"
    assert meta2['raw_files'][1]['raw_file_url'] == "https://test.com/f2.csv"
