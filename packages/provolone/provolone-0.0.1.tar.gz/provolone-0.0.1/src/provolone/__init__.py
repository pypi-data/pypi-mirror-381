# src/provolone/__init__.py
from __future__ import annotations
import json
from pathlib import Path
import urllib.request
import urllib.parse
from .datasets import get as _get, registry
from .snapshots import write_snapshot, read_snapshot, _snapshot_paths
from .utils.file_meta import extract_file_metadata_for_tagging

__all__ = [
    "__version__",
    "load",
    "load_with_metadata",
    "freeze",
    "recreate",
    "tag",
    "download",
    "registry",
    "list_datasets",
]
__version__ = "0.0.0"


def load_with_metadata(
    name: str,
    *,
    snapshot: str | None = None,
    force: bool = False,
    data_dir: str | Path | None = None,
    snapshot_dir: str | Path | None = None,
    **params,
):
    """Load a dataset and return both DataFrame and metadata.

    Args:
        name: Dataset name
        snapshot: Optional snapshot label to load from
        force: Force fresh computation, bypassing cache
        data_dir: Optional path to the directory containing this dataset's data files.
                 Points directly to where the data files are located (not a root directory).
                 Falls back to params['data_dir'] or params['data_root'].
        snapshot_dir: Optional path to the directory containing this dataset's snapshots.
                     Points directly to where snapshots for this dataset are stored (not a root directory).
                     Falls back to params['snapshot_dir'] or params['snapshot_root'].
        **params: Dataset-specific parameters. Also accepts 'raw_file_url',
                 'raw_file_source', and 'raw_file_notes' for recording file provenance metadata
                 (used as fallback for files without sidecar metadata). Can also include
                 'data_root' and 'snapshot_root' for root directories with automatic name appending.

    Returns:
        tuple[pd.DataFrame, dict]: DataFrame and metadata dict. The metadata may include
                                  a 'raw_files' field (list) with file provenance information
                                  for each raw file used.
    """
    # Handle data_dir: prefer direct argument, fall back to params
    # Keep data_root for backward compatibility (it's a root with name appended)
    # data_dir is new and points directly to the dataset directory
    if data_dir is not None:
        params["data_dir"] = data_dir
    elif "data_dir" in params:
        data_dir = params["data_dir"]
    # Note: data_root is kept in params for backward compatibility
    # BaseDataset will handle it appropriately

    # Handle snapshot_dir: prefer direct argument, fall back to params
    # Track if snapshot_dir was passed as direct argument for dataset_specific flag
    # Also handle snapshot_root (root directory with name appended)
    snapshot_dir_is_direct = snapshot_dir is not None
    if snapshot_dir is not None:
        params["snapshot_dir"] = snapshot_dir
    elif "snapshot_dir" in params:
        snapshot_dir = params["snapshot_dir"]
    # Note: snapshot_root is kept in params for BaseDataset to handle

    if snapshot:
        # Extract snapshot_dir/snapshot_root if provided, but don't pass it to the dataset
        snapshot_dir_for_read = params.pop("snapshot_dir", None)
        snapshot_root_for_read = params.pop("snapshot_root", None)

        # If snapshot_root is provided, use it with name appending (not dataset_specific)
        if snapshot_root_for_read is not None:
            snapshot_dir_for_read = snapshot_root_for_read
            snapshot_dir_is_direct = False

        # Get snapshot and read with metadata
        p = _snapshot_paths(
            name,
            snapshot,
            snapshot_dir_for_read,
            dataset_specific=snapshot_dir_is_direct,
        )
        if not p.data_path.exists():
            raise FileNotFoundError(f"Snapshot not found: {p.data_path}")
        df, meta = read_snapshot(
            name,
            snapshot,
            snapshot_dir=snapshot_dir_for_read,
            dataset_specific=snapshot_dir_is_direct,
        )
        # Update metadata to reflect snapshot hit and current params
        meta.update({"params": params, "cache": "snapshot-hit"})
        # Re-add snapshot_dir/snapshot_root to params for consistency if it was provided
        if snapshot_dir_for_read is not None and snapshot_root_for_read is None:
            params["snapshot_dir"] = snapshot_dir_for_read
        elif snapshot_root_for_read is not None:
            params["snapshot_root"] = snapshot_root_for_read
        return df, meta
    ds = _get(name)(**params)
    lr = ds.load(force=force)
    return lr.df, lr.meta


def load(
    name: str,
    *,
    snapshot: str | None = None,
    force: bool = False,
    data_dir: str | Path | None = None,
    snapshot_dir: str | Path | None = None,
    **params,
):
    """Load a dataset and return the DataFrame.

    Args:
        name: Dataset name
        snapshot: Optional snapshot label to load from
        force: Force fresh computation, bypassing cache
        data_dir: Optional path to the directory containing this dataset's data files.
                 Points directly to where the data files are located (not a root directory).
                 Falls back to params['data_dir'] or params['data_root'].
        snapshot_dir: Optional path to the directory containing this dataset's snapshots.
                     Points directly to where snapshots for this dataset are stored (not a root directory).
                     Falls back to params['snapshot_dir'] or params['snapshot_root'].
        **params: Dataset-specific parameters. Also accepts 'raw_file_url', 'raw_file_source',
                 and 'raw_file_notes' for recording file provenance metadata (used as fallback
                 for files without sidecar metadata). Can also include 'data_root' and 'snapshot_root'
                 for root directories with automatic name appending.

    Returns:
        pd.DataFrame: The loaded dataset
    """
    df, _ = load_with_metadata(
        name,
        snapshot=snapshot,
        force=force,
        data_dir=data_dir,
        snapshot_dir=snapshot_dir,
        **params,
    )
    return df


def freeze(
    name: str,
    *,
    snapshot: str,
    force: bool = False,
    data_dir: str | Path | None = None,
    snapshot_dir: str | Path | None = None,
    **params,
):
    """Create an immutable snapshot of a dataset.

    This function computes the dataset fresh and saves it as an immutable snapshot
    that can be loaded later. Snapshots are useful for creating reproducible
    versions of datasets at specific points in time.

    Args:
        name: Dataset name
        snapshot: Label for the snapshot (e.g., "2024-01-15", "v1.0")
        force: Allow overwriting existing snapshots (default: False)
        data_dir: Optional path to the directory containing this dataset's data files.
                 Points directly to where the data files are located (not a root directory).
                 Falls back to params['data_dir'] or params['data_root'].
        snapshot_dir: Optional path to the directory containing this dataset's snapshots.
                     Points directly to where snapshots for this dataset are stored (not a root directory).
                     Falls back to params['snapshot_dir'] or params['snapshot_root'].
        **params: Dataset-specific parameters. Also accepts 'raw_file_url',
                 'raw_file_source', and 'raw_file_notes' for recording file provenance metadata.
                 Can also include 'data_root' and 'snapshot_root' for root directories with
                 automatic name appending.

    Returns:
        Path: Root path of the created snapshot

    Raises:
        FileExistsError: If snapshot already exists and force=False
    """
    # Handle data_dir: prefer direct argument, fall back to params
    # Keep data_root for backward compatibility (it's a root with name appended)
    # data_dir is new and points directly to the dataset directory
    if data_dir is not None:
        params["data_dir"] = data_dir
    # Note: data_root is kept in params for backward compatibility
    # BaseDataset will handle it appropriately

    # Handle snapshot_dir: prefer direct argument, fall back to params
    # Track if snapshot_dir was passed as direct argument for dataset_specific flag
    # Also handle snapshot_root (root directory with name appended)
    snapshot_dir_is_direct = snapshot_dir is not None
    if snapshot_dir is not None:
        params["snapshot_dir"] = snapshot_dir

    # Extract snapshot_dir/snapshot_root before creating dataset to pass it to write_snapshot
    snapshot_dir_for_write = params.get("snapshot_dir")
    snapshot_root_for_write = params.get("snapshot_root")

    # If snapshot_root is provided, use it (not dataset_specific)
    if snapshot_root_for_write is not None:
        snapshot_dir_for_write = snapshot_root_for_write
        snapshot_dir_is_direct = False

    ds = _get(name)(**params)
    lr = ds.load(force=True)  # compute fresh

    # Extract extra metadata from LoadResult (e.g., raw_files)
    extra_metadata = {}
    if "raw_files" in lr.meta:
        extra_metadata["raw_files"] = lr.meta["raw_files"]
    # Backward compatibility: also check for old raw_file_meta
    elif "raw_file_meta" in lr.meta:
        extra_metadata["raw_file_meta"] = lr.meta["raw_file_meta"]

    # Capture method sources for reproducibility (recipe)
    from .utils.source import extract_method_recipe

    recipe = {}
    for method_name in ["fetch", "parse", "transform"]:
        method_recipe = extract_method_recipe(ds, method_name)
        if method_recipe is not None:
            recipe[method_name] = method_recipe
    if recipe:
        extra_metadata["recipe"] = recipe

    # For freeze operations, snapshots should not be overwritable unless force=True
    return write_snapshot(
        name,
        lr.df,
        snapshot,
        params=ds.params,
        dataset_name=name,
        allow_overwrite=force,
        snapshot_dir=snapshot_dir_for_write,
        extra_metadata=extra_metadata if extra_metadata else None,
        dataset_specific=snapshot_dir_is_direct,
    )


def recreate(
    name: str,
    *,
    snapshot: str,
    snapshot_dir: str | Path | None = None,
    output_dir: str | Path | None = None,
    execute_potentially_unsafe: bool = False,
    **params,
) -> Path:
    """Recreate a dataset from its snapshot recipe.

    This function rebuilds a dataset using only the captured source code stored
    in the snapshot metadata. It does not import any user modules, making the
    snapshot portable and reproducible even if the original code has changed.

    **WARNING**: This function executes code from the snapshot recipe. Only use
    snapshots from trusted sources. You must explicitly set execute_potentially_unsafe=True
    to acknowledge this risk.

    Args:
        name: Dataset name
        snapshot: Snapshot label to recreate from
        snapshot_dir: Optional path to the directory containing this dataset's snapshots.
                     Points directly to where snapshots for this dataset are stored.
        output_dir: Optional output directory for recreated data. If not provided,
                   creates a subdirectory next to the snapshot.
        execute_potentially_unsafe: Must be set to True to acknowledge the security
                                   risk of executing code from the snapshot recipe.
                                   Only use snapshots from trusted sources.
        **params: Dataset-specific parameters to use during recreation

    Returns:
        Path: Path to the recreated data file

    Raises:
        FileNotFoundError: If snapshot doesn't exist
        ValueError: If snapshot doesn't contain recipe data or if execute_potentially_unsafe
                   is not set to True
    """
    from pathlib import Path
    import pandas as pd
    from .datasets.base import BaseDataset

    # Security check: user must explicitly acknowledge the risk
    if not execute_potentially_unsafe:
        raise ValueError(
            "The recreate function executes code from the snapshot recipe. "
            "This could be unsafe if the snapshot is from an untrusted source. "
            "To proceed, you must explicitly set execute_potentially_unsafe=True. "
            "Only use snapshots from trusted sources."
        )

    # Determine if snapshot_dir is dataset-specific
    snapshot_dir_is_direct = snapshot_dir is not None

    # Read the snapshot metadata to get the recipe
    p = _snapshot_paths(
        name,
        snapshot,
        snapshot_dir,
        dataset_specific=snapshot_dir_is_direct,
    )

    if not p.data_path.exists():
        raise FileNotFoundError(f"Snapshot not found: {p.data_path}")

    # Read metadata to get the recipe
    from .snapshots import read_df_from_path

    _, meta = read_df_from_path(p.data_path)

    if "recipe" not in meta:
        raise ValueError(
            f"Snapshot '{snapshot}' for dataset '{name}' does not contain recipe data. "
            f"This snapshot was created before recipe support was added. "
            f"Please re-freeze the dataset to enable recreation."
        )

    recipe = meta["recipe"]

    # Create a throwaway BaseDataset subclass from the captured sources
    # Use a clean namespace to avoid importing user modules
    namespace = {
        "pd": pd,
        "Path": Path,
        "BaseDataset": BaseDataset,
    }

    # Compile and execute each method in the namespace
    for method_name in ["fetch", "parse", "transform"]:
        if method_name in recipe:
            source = recipe[method_name]["source"]
            # Compile the method source
            code = compile(source, f"<recipe-{method_name}>", "exec")
            exec(code, namespace)

    # Create the dataset class dynamically
    # We need to make it non-abstract by ensuring parse exists
    class RecreatedDataset(BaseDataset):
        # Placeholder parse if not in recipe (to satisfy ABC)
        def parse(self, raw):
            raise NotImplementedError("parse not in recipe")

    # Set the name and bind the methods
    RecreatedDataset.name = name

    # Bind methods from namespace if they exist
    if "fetch" in namespace:
        RecreatedDataset.fetch = namespace["fetch"]
    if "parse" in namespace:
        RecreatedDataset.parse = namespace["parse"]
    if "transform" in namespace:
        RecreatedDataset.transform = namespace["transform"]

    # Create an instance and run the pipeline
    ds = RecreatedDataset(**params)

    # Execute the pipeline: fetch -> parse -> transform
    raw = ds.fetch()
    df = ds.parse(raw)
    df = ds.transform(df)
    df = ds._standardize(df)

    # Determine output path
    if output_dir is not None:
        output_path = Path(output_dir)
    else:
        # Create a "recreated" subdirectory next to the snapshot
        output_path = p.root / "recreated"

    output_path.mkdir(parents=True, exist_ok=True)

    # Write the recreated data
    from .snapshots import _ext

    ext = _ext()
    output_file = output_path / f"data.{ext}"

    from .snapshots import write_df_to_path

    write_df_to_path(
        df,
        output_file,
        params=params,
        dataset_name=name,
        extra_metadata={
            "recreated_from": snapshot,
            "recipe_hashes": {k: v["hash"] for k, v in recipe.items()},
        },
    )

    return output_file


def tag(
    file_path: str,
    *,
    raw_file_url: str | None = None,
    raw_file_source: str | None = None,
    raw_file_notes: str | None = None,
    **metadata,
):
    """Tag a file with metadata, creating a sidecar .meta.json file.

    Args:
        file_path: Path to the file to tag
        raw_file_url: URL where the file was obtained
        raw_file_source: Data provider/source (e.g., "Bureau of Labor Statistics")
        raw_file_notes: Notes about the file or its acquisition
        **metadata: Additional metadata fields to include

    Returns:
        Path: Path to the created metadata file

    Examples:
        >>> tag("data.csv", raw_file_url="https://example.com/data.csv",
        ...     raw_file_source="Example Data Provider",
        ...     raw_file_notes="Downloaded on 2024-12-27")
        Path('data.meta.json')
    """
    file_path = Path(file_path)

    # Generate comprehensive file metadata
    file_meta = extract_file_metadata_for_tagging(
        file_path, url=raw_file_url, source=raw_file_source, notes=raw_file_notes
    )

    # Add any additional metadata fields
    if metadata:
        file_meta.update(metadata)

    # Create sidecar metadata file path
    if file_path.suffix:
        # Remove file extension and add .meta.json
        meta_path = file_path.with_suffix(".meta.json")
    else:
        # If no extension, just append .meta.json
        meta_path = file_path.with_suffix(file_path.suffix + ".meta.json")

    # Write metadata to sidecar file
    with open(meta_path, "w") as f:
        json.dump(file_meta, f, indent=2, default=str)

    return meta_path


def download(
    url: str,
    destination: str | Path | None = None,
    *,
    source: str | None = None,
    notes: str | None = None,
) -> Path:
    """Download a file from a URL and automatically tag it with metadata.

    This function downloads a file from the specified URL and automatically
    creates a metadata sidecar file using the tag() function. The URL is
    recorded as the raw_file_url in the metadata.

    Args:
        url: URL to download from
        destination: Optional destination path. If not provided, saves to current directory
                    with filename from URL
        source: Optional data provider/source (e.g., "Bureau of Labor Statistics")
        notes: Optional notes about the download to include in metadata

    Returns:
        Path: Path to the downloaded file

    Examples:
        >>> # Download to current directory
        >>> path = download("https://example.com/data.csv")
        >>> print(path)
        Path('data.csv')

        >>> # Download to specific location with source and notes
        >>> path = download(
        ...     "https://example.com/data.csv",
        ...     destination="/path/to/my_data.csv",
        ...     source="Bureau of Labor Statistics",
        ...     notes="Downloaded on 2024-12-27 for analysis"
        ... )
        Path('/path/to/my_data.csv')
    """
    # Determine destination path
    if destination is None:
        # Extract filename from URL
        filename = Path(urllib.parse.urlparse(url).path).name
        if not filename:
            raise ValueError(f"Could not determine filename from URL: {url}")
        dest_path = Path(filename)
    else:
        dest_path = Path(destination)

    # Create parent directory if it doesn't exist
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Download the file
    try:
        urllib.request.urlretrieve(url, dest_path)
    except Exception as e:
        raise RuntimeError(f"Failed to download from {url}: {e}") from e

    # Tag the file with metadata
    tag(str(dest_path), raw_file_url=url, raw_file_source=source, raw_file_notes=notes)

    return dest_path


def _load_sidecar_metadata(file_path: Path) -> dict | None:
    """Load metadata from sidecar .meta.json file if it exists.

    Args:
        file_path: Path to the data file

    Returns:
        dict | None: Metadata dictionary or None if sidecar doesn't exist
    """
    if file_path.suffix:
        meta_path = file_path.with_suffix(".meta.json")
    else:
        meta_path = file_path.with_suffix(file_path.suffix + ".meta.json")

    if meta_path.exists():
        try:
            with open(meta_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            # If we can't read the metadata file, just ignore it
            pass

    return None


def list_datasets():
    """Return a list of all registered dataset names.

    Returns:
        list[str]: List of available dataset names
    """
    return list(registry.keys())
