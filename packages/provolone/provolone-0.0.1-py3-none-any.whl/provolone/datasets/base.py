# src/provolone/datasets/base.py
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from ..config import cfg
from ..snapshots import cache_path, snapshot_path, read_df, write_df


@dataclass
class LoadResult:
    """Result of loading a dataset.

    Attributes:
        df: The loaded pandas DataFrame
        cache_file: Path to the cached data file
        meta: Metadata dictionary with information about the dataset
    """

    df: pd.DataFrame
    cache_file: Path
    meta: dict


class BaseDataset(ABC):
    """Base class for all datasets in provolone.

    This abstract base class defines the interface that all datasets must implement.
    It provides caching, snapshot management, and standardization functionality.

    Attributes:
        name: Unique identifier for the dataset
        frequency: Data frequency ('m' for monthly, 'd' for daily, etc.)
    """

    name: str
    frequency: str = "m"

    def __init__(self, **params):
        """Initialize dataset with parameters.

        Args:
            **params: Dataset-specific parameters. May include 'snapshot'
                     for snapshot loading, plus dataset-specific keys like
                     'vintage', 'table', 'freq', 'detail', etc.
                     Also accepts 'data_dir' (direct path), 'data_root' (root with name appended),
                     'snapshot_dir' (direct path), and 'snapshot_root' (root with name appended)
                     for dataset-specific path configuration.

                     For raw file metadata recording, you can provide:
                     - 'raw_file_url': URL where the file was obtained (fallback for files without sidecar)
                     - 'raw_file_source': Data provider (fallback for files without sidecar)
                     - 'raw_file_notes': Custom notes (fallback for files without sidecar)

                     For multiple files, use the tag() or download() functions to attach
                     metadata to each file via sidecar .meta.json files. The parameters
                     above serve as fallbacks for files without sidecar metadata.
        """
        # Extract path overrides from params before storing them
        # data_dir is new: points directly to dataset directory
        self._data_dir = params.pop("data_dir", None)
        # data_root is legacy: root directory with name appended
        self._data_root = params.pop("data_root", None)

        # snapshot_dir is new: points directly to dataset's snapshot directory
        self._snapshot_dir = params.pop("snapshot_dir", None)
        # snapshot_root is legacy: root directory with name appended
        self._snapshot_root = params.pop("snapshot_root", None)

        # params may include 'snapshot' plus dataset-specific keys like vintage/table/etc.
        self.params = params
        self._suffix = self._cache_suffix()
        self._snapshot_label: str | None = params.get("snapshot")

    @property
    def data_dir(self) -> Path:
        """Get data directory path for this dataset.

        If a dataset-specific data_dir was provided, use it directly.
        If a legacy data_root was provided, append dataset name to it.
        Otherwise, fall back to global data_root and append dataset name.
        """
        if self._data_dir is not None:
            return Path(self._data_dir)
        # Use data_root (either custom or global) with dataset name subdirectory
        if self._data_root is not None:
            return Path(self._data_root) / self.name
        # Default: use global data_root with dataset name subdirectory
        return cfg.data_root / self.name

    @property
    def snapshot_dir(self) -> Path:
        """Get snapshot directory path for this dataset.

        If a dataset-specific snapshot_dir was provided, use it directly.
        If a legacy snapshot_root was provided, append dataset name to it.
        Otherwise, fall back to global snapshots_root and append dataset name.
        """
        if self._snapshot_dir is not None:
            return Path(self._snapshot_dir)
        # Use snapshot_root (either custom or global) with dataset name subdirectory
        if self._snapshot_root is not None:
            return Path(self._snapshot_root) / self.name
        # Default: use global snapshots_root with dataset name subdirectory
        return cfg.snapshots_root / self.name

    def _cache_suffix(self) -> str | None:
        """Generate cache suffix based on parameters that affect output.

        Include only params that change the output schema/values to ensure
        proper cache invalidation when meaningful parameters change.
        Also includes path overrides to ensure cache isolation.

        Returns:
            Optional cache suffix string, or None if no relevant parameters
        """
        keys = ("vintage", "table", "freq", "detail")
        interesting = {k: self.params[k] for k in keys if k in self.params}

        # Add path overrides to cache key for isolation
        if self._data_dir is not None:
            interesting["data_dir"] = str(self._data_dir)
        if self._data_root is not None:
            interesting["data_root"] = str(self._data_root)
        if self._snapshot_dir is not None:
            interesting["snapshot_dir"] = str(self._snapshot_dir)
        if self._snapshot_root is not None:
            interesting["snapshot_root"] = str(self._snapshot_root)

        if not interesting:
            return None
        parts = [
            f"{k}-{hash(str(interesting[k])) % 100000}" for k in sorted(interesting)
        ]
        return "__".join(parts)

    def load(self, force: bool = False) -> LoadResult:
        """Load the dataset with caching and snapshot support.

        This method implements the core loading logic with intelligent caching.
        It first checks for snapshots if a snapshot label is provided, then
        checks the cache, and finally computes the dataset from scratch if needed.

        Args:
            force: If True, bypass all caches and compute fresh data

        Returns:
            LoadResult containing the DataFrame, cache file path, and metadata
        """
        # If a snapshot label is given, read that immutable artifact if present
        if self._snapshot_label:
            snap_path = snapshot_path(
                self.name,
                self._snapshot_label,
                self._suffix,
                self.snapshot_dir,
                dataset_specific=True,
            )
            if snap_path.exists() and not force:
                df, meta = read_df(snap_path)
                meta.update({"cache": "snapshot-hit"})
                return LoadResult(df, snap_path, meta)
            # else compute below and write the snapshot

        # Normal cache path for speed in active dev
        cache = cache_path(
            self.name, self._suffix, self.snapshot_dir, dataset_specific=True
        )
        if cache.exists() and not force:
            df, meta = read_df(cache)
            # Update metadata to include cache status and current params
            meta.update({"cache": "hit"})
            return LoadResult(df, cache, meta)

        # Compute fresh
        raw = self.fetch()

        # Extract raw file metadata - support both single files and lists of files
        raw_files_meta = None
        if raw is not None:
            # Normalize to list for uniform processing
            raw_list = []
            if isinstance(raw, (list, tuple)):
                raw_list = list(raw)
            elif isinstance(raw, (str, Path)) or hasattr(raw, "__fspath__"):
                raw_list = [raw]

            # Extract metadata for each file
            if raw_list:
                try:
                    from ..utils.file_meta import extract_file_metadata
                    from .. import _load_sidecar_metadata

                    raw_files_meta = []
                    for raw_item in raw_list:
                        raw_path = Path(raw_item)

                        # First, try to load sidecar metadata
                        sidecar_meta = _load_sidecar_metadata(raw_path)

                        # Use params as fallback only if sidecar doesn't have metadata
                        url = self.params.get("raw_file_url")
                        source = self.params.get("raw_file_source")
                        notes = self.params.get("raw_file_notes")

                        # Prefer sidecar metadata over params
                        if sidecar_meta:
                            if "raw_file_url" in sidecar_meta:
                                url = sidecar_meta.get("raw_file_url")
                            if "raw_file_source" in sidecar_meta:
                                source = sidecar_meta.get("raw_file_source")
                            if "raw_file_notes" in sidecar_meta:
                                notes = sidecar_meta.get("raw_file_notes")

                        file_meta = extract_file_metadata(
                            raw_path,
                            url=url,
                            source=source,
                            notes=notes,
                            sidecar_meta=sidecar_meta,
                        )
                        raw_files_meta.append(file_meta)
                except Exception:
                    # If metadata extraction fails, continue without it
                    raw_files_meta = None

        df = self.transform(self.parse(raw))
        df = self._standardize(df)

        # Write normal cache with metadata (including raw file metadata if available)
        extra_metadata = {"raw_files": raw_files_meta} if raw_files_meta else {}
        write_df(
            df,
            cache,
            params=self.params,
            dataset_name=self.name,
            extra_metadata=extra_metadata,
        )

        # Read back the metadata that was written
        df, meta = read_df(cache)
        meta.update({"cache": "miss"})

        # If snapshot requested, write-once (unless force=True)
        if self._snapshot_label:
            snap_path = snapshot_path(
                self.name,
                self._snapshot_label,
                self._suffix,
                self.snapshot_dir,
                dataset_specific=True,
            )
            if snap_path.exists() and not force:
                # Don't overwrite; keep the first frozen copy
                pass
            else:
                write_df(
                    df,
                    snap_path,
                    params=self.params,
                    dataset_name=self.name,
                    extra_metadata=extra_metadata,
                )
            return LoadResult(df, snap_path, meta)

        return LoadResult(df, cache, meta)

    # -------- Hooks --------
    def fetch(self):
        """Fetch raw data for the dataset.

        This method should download, locate, or prepare the raw data needed
        for the dataset. It can return a file path, URL, or any object that
        the parse() method can handle. For datasets with multiple source files,
        return a list or tuple of file paths.

        Returns:
            Raw data source (file path, list of file paths, data object, etc.)
            or None if data is in-memory
        """
        ...

    @abstractmethod
    def parse(self, raw) -> pd.DataFrame:
        """Parse raw data into a pandas DataFrame.

        This method converts the raw data returned by fetch() into a standardized
        pandas DataFrame. This is the only required method that subclasses must implement.

        Args:
            raw: Raw data returned by fetch()

        Returns:
            pd.DataFrame: Parsed data as a DataFrame
        """
        ...

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply dataset-specific transformations.

        Override this method to apply custom transformations like filtering,
        reshaping, calculating derived columns, etc. The default implementation
        returns the DataFrame unchanged.

        Args:
            df: DataFrame returned by parse()

        Returns:
            pd.DataFrame: Transformed DataFrame
        """
        return df

    def _standardize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply standardization to the DataFrame.

        This method applies consistent formatting like column name normalization
        and index sorting. It's called automatically by load() after transform().

        Args:
            df: DataFrame to standardize

        Returns:
            pd.DataFrame: Standardized DataFrame
        """
        df = df.copy()
        # Per-dataset override takes precedence if defined; else fall back to global config
        normalize = getattr(self, "normalize_columns", None)
        if normalize is None:
            normalize = bool(cfg.normalize_columns)
        if normalize:
            # lightweight snake_case: trim + lowercase + spaces->underscores
            df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
        # Sort time index if present (no change to names)
        if isinstance(df.index, pd.DatetimeIndex):
            df = df.sort_index()
        return df
