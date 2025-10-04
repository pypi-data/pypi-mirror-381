from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
import json
import datetime as dt
import pandas as pd
from .config import cfg
from .utils.index_meta import index_fingerprint
from .utils.hash import hash_df, hash_file

# Default label for regular cache operations
DEFAULT_SNAPSHOT_LABEL = "_default"


@dataclass
class SnapshotPaths:
    root: Path
    data_path: Path
    manifest_path: Path


def _ext() -> str:
    return "feather" if cfg.io_format == "feather" else "parquet"


def _snapshot_paths(
    name: str,
    label: str,
    snapshot_dir: Path | str | None = None,
    dataset_specific: bool = False,
) -> SnapshotPaths:
    """Get snapshot paths for a dataset.

    Args:
        name: Dataset name
        label: Snapshot label
        snapshot_dir: Optional custom snapshot directory
        dataset_specific: If True, snapshot_dir points directly to this dataset's snapshot directory.
                         If False, snapshot_dir is a root directory and name will be appended.

    Returns:
        SnapshotPaths with root, data_path, and manifest_path
    """
    safe = label.replace("/", "_")
    if snapshot_dir is not None:
        base_dir = Path(snapshot_dir)
    else:
        base_dir = cfg.snapshots_root

    # If dataset_specific is True, snapshot_dir already points to the dataset's directory
    # Otherwise, append the dataset name to get to the dataset's directory
    if dataset_specific and snapshot_dir is not None:
        root = base_dir / safe
    else:
        root = base_dir / name / safe

    root.mkdir(parents=True, exist_ok=True)
    ext = "feather" if cfg.io_format == "feather" else "parquet"
    return SnapshotPaths(
        root=root,
        data_path=root / f"data.{ext}",
        manifest_path=root / "manifest.json",
    )


def _meta_path(data_path: Path) -> Path:
    """Get metadata path for data file (consolidated metadata)"""
    return data_path.with_suffix(data_path.suffix + ".meta.json")


def cache_path(
    name: str,
    suffix: str | None = None,
    snapshot_dir: Path | str | None = None,
    dataset_specific: bool = False,
) -> Path:
    """Get the path for a cached dataset using the snapshot system.

    Args:
        name: Dataset name
        suffix: Optional suffix for cache differentiation
        snapshot_dir: Optional custom snapshot directory, falls back to global config
        dataset_specific: If True, snapshot_dir points directly to this dataset's snapshot directory.
                         If False, snapshot_dir is a root directory and name will be appended.

    Returns:
        Path to the cache file
    """
    # For cache, we use the special _default label
    label = DEFAULT_SNAPSHOT_LABEL
    if suffix:
        label = f"{DEFAULT_SNAPSHOT_LABEL}__{suffix}"

    p = _snapshot_paths(name, label, snapshot_dir, dataset_specific)
    return p.data_path


def snapshot_path(
    name: str,
    label: str,
    suffix: str | None = None,
    snapshot_dir: Path | str | None = None,
    dataset_specific: bool = False,
) -> Path:
    """Get the path for a snapshot dataset.

    Args:
        name: Dataset name
        label: Snapshot label
        suffix: Optional suffix for snapshot differentiation
        snapshot_dir: Optional custom snapshot directory, falls back to global config
        dataset_specific: If True, snapshot_dir points directly to this dataset's snapshot directory.
                         If False, snapshot_dir is a root directory and name will be appended.

    Returns:
        Path to the snapshot file
    """
    # Handle suffix by modifying the label
    final_label = label
    if suffix:
        final_label = f"{label}__{suffix}"

    p = _snapshot_paths(name, final_label, snapshot_dir, dataset_specific)
    return p.data_path


def read_snapshot(
    name: str,
    label: str = DEFAULT_SNAPSHOT_LABEL,
    suffix: str = None,
    snapshot_dir: Path | str | None = None,
    dataset_specific: bool = False,
) -> tuple[pd.DataFrame, dict]:
    """Read DataFrame from snapshot and return with metadata.

    Args:
        name: Dataset name
        label: Snapshot label (defaults to '_default' for cache)
        suffix: Optional suffix for label
        snapshot_dir: Optional custom snapshot directory, falls back to global config
        dataset_specific: If True, snapshot_dir points directly to this dataset's snapshot directory.
                         If False, snapshot_dir is a root directory and name will be appended.

    Returns:
        tuple[pd.DataFrame, dict]: DataFrame and metadata dict
    """
    # Handle suffix by modifying the label
    final_label = label
    if suffix:
        final_label = f"{label}__{suffix}"

    p = _snapshot_paths(name, final_label, snapshot_dir, dataset_specific)
    return read_df_from_path(p.data_path)


def read_df_from_path(path: Path) -> tuple[pd.DataFrame, dict]:
    """Read DataFrame from file path and return with metadata."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix == ".feather":
        df = pd.read_feather(path)
    elif path.suffix == ".parquet":
        df = pd.read_parquet(path)
    else:
        raise ValueError(f"Unsupported file: {path}")

    # restore index using metadata from consolidated file
    mp = _meta_path(path)
    meta = {}
    if mp.exists():
        try:
            meta = json.loads(mp.read_text())
            # Use index_cols for backward compatibility, or extract from fingerprint/index
            idx_cols = meta.get("index_cols")
            if not idx_cols and "fingerprint" in meta:
                idx_cols = meta["fingerprint"].get("names", [])
            elif not idx_cols and "index" in meta:
                idx_cols = meta["index"].get("names", [])

            if idx_cols:
                cols = [c for c in idx_cols if c in df.columns]
                if cols:
                    df = df.set_index(cols)
                elif len(df.columns) > 0:
                    take = len(idx_cols) if len(idx_cols) > 0 else 1
                    df = df.set_index(list(df.columns[:take]))
        except (json.JSONDecodeError, FileNotFoundError):
            meta = {}

    # Return the consolidated metadata (already loaded above)
    return df, meta


def write_snapshot(
    name: str,
    df: pd.DataFrame,
    label: str = DEFAULT_SNAPSHOT_LABEL,
    suffix: str = None,
    *,
    params: dict = None,
    dataset_name: str = None,
    allow_overwrite: bool = None,
    snapshot_dir: Path | str | None = None,
    extra_metadata: dict = None,
    dataset_specific: bool = False,
) -> Path:
    """Write DataFrame to snapshot with metadata.

    Args:
        name: Dataset name
        df: DataFrame to write
        label: Snapshot label (defaults to '_default' for cache)
        suffix: Optional suffix for label
        params: Dataset parameters
        dataset_name: Name of dataset (for metadata, defaults to name)
        allow_overwrite: Whether to allow overwriting existing snapshots.
                        If None, defaults to True for '_default' label, False for others.
        snapshot_dir: Optional custom snapshot directory, falls back to global config
        extra_metadata: Additional metadata to include (e.g., raw_file_meta)
        dataset_specific: If True, snapshot_dir points directly to this dataset's snapshot directory.
                         If False, snapshot_dir is a root directory and name will be appended.

    Returns:
        Path: Root path of the snapshot
    """
    # Handle suffix by modifying the label
    final_label = label
    if suffix:
        final_label = f"{label}__{suffix}"

    p = _snapshot_paths(name, final_label, snapshot_dir, dataset_specific)

    # Default overwrite behavior: allow for cache, protect for snapshots
    if allow_overwrite is None:
        allow_overwrite = label == DEFAULT_SNAPSHOT_LABEL

    # Check overwrite protection
    if p.data_path.exists() and not allow_overwrite:
        if label == DEFAULT_SNAPSHOT_LABEL:
            # This shouldn't happen for cache, but just in case
            pass  # Allow overwrite for cache
        else:
            raise FileExistsError(
                f"Snapshot '{final_label}' for dataset '{name}' already exists. Use allow_overwrite=True to overwrite."
            )

    write_df_to_path(
        df,
        p.data_path,
        params=params,
        dataset_name=dataset_name or name,
        extra_metadata=extra_metadata,
    )
    return p.root


def write_df_to_path(
    df: pd.DataFrame,
    path: Path,
    *,
    params: dict = None,
    dataset_name: str = None,
    extra_metadata: dict = None,
) -> None:
    """Write DataFrame to file with metadata."""
    # Use dataset_name if provided
    effective_dataset_name = dataset_name

    # Materialize index as columns for consistent round-trip across formats
    if isinstance(df.index, pd.MultiIndex) or (df.index.name is not None):
        tmp = df.reset_index()
    else:
        tmp = df

    if path.suffix == ".feather":
        tmp.to_feather(path, compression=cfg.io_compression)
    elif path.suffix == ".parquet":
        tmp.to_parquet(path, compression=cfg.io_compression, index=False)
    else:
        raise ValueError(f"Unsupported file: {path}")

    # Write comprehensive metadata to single file (includes both data and index info)
    meta_path = _meta_path(path)

    # Create comprehensive metadata that includes index info
    comprehensive_meta = {
        # Data metadata
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "version": __import__("provolone").__version__,
        "normalize_columns": (
            bool(getattr(df, "_normalized", True))
            if hasattr(df, "_normalized")
            else None
        ),
        "params": params or {},
        "io": {"format": cfg.io_format, "compression": cfg.io_compression},
        "shape": {"rows": int(df.shape[0]), "cols": int(df.shape[1])},
        "index": index_fingerprint(df.index),
        "content_hash": hash_df(df),
        "dataset": effective_dataset_name,
        "extras": {},
        # Index metadata (for backward compatibility)
        "index_cols": index_fingerprint(df.index)["names"],
        "fingerprint": index_fingerprint(df.index),
    }

    # Add extra metadata if provided
    if extra_metadata:
        comprehensive_meta.update(extra_metadata)

    # Add file info after file is written
    if path.exists():
        comprehensive_meta["file"] = {
            "bytes": path.stat().st_size,
            "sha256": hash_file(path),
        }

    meta_path.write_text(json.dumps(comprehensive_meta, indent=2, default=str))


def list_snapshot_labels(
    name: str, snapshot_dir: Path | str | None = None
) -> list[str]:
    """List all snapshot labels for a dataset.

    Args:
        name: Dataset name
        snapshot_dir: Optional custom snapshot directory, falls back to global config
    """
    base_dir = Path(snapshot_dir) if snapshot_dir is not None else cfg.snapshots_root
    base = base_dir / name
    if not base.exists():
        return []
    return sorted([d.name for d in base.iterdir() if d.is_dir()])


# Compatibility aliases for existing code that uses paths directly
def read_df(path: Path) -> tuple[pd.DataFrame, dict]:
    """Compatibility alias for path-based reads."""
    return read_df_from_path(path)


def write_df(
    df: pd.DataFrame,
    path: Path,
    *,
    params: dict = None,
    dataset_name: str = None,
    extra_metadata: dict = None,
) -> None:
    """Compatibility alias for path-based writes."""
    write_df_to_path(
        df,
        path,
        params=params,
        dataset_name=dataset_name,
        extra_metadata=extra_metadata,
    )
