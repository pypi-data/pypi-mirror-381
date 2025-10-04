from __future__ import annotations
import typer
from typing import Optional
from . import (
    load as _load,
    freeze as _freeze,
    recreate as _recreate,
    tag as _tag,
    download as _download,
)
from .snapshots import list_snapshot_labels

app = typer.Typer(help="provolone CLI")


@app.command()
def build(
    name: str,
    snapshot: Optional[str] = typer.Option(
        None, help="Label of snapshot to build from"
    ),
    data_dir: Optional[str] = typer.Option(
        None,
        "--data-dir",
        help="Path to directory containing this dataset's data files",
    ),
    snapshot_dir: Optional[str] = typer.Option(
        None,
        "--snapshot-dir",
        help="Path to directory containing this dataset's snapshots",
    ),
    params: list[str] = typer.Option(None, help="key=val pairs"),
    head: int = typer.Option(0, help="Print DataFrame head(n)"),
):
    """Build a dataset and display basic information.

    This command processes and caches a dataset without loading it into memory.
    Use the --head option to display the first N rows.

    Examples:
        provolone build example
        provolone build example --params vintage=2024
        provolone build example --snapshot 2024-01-15
        provolone build example --head 10
        provolone build example --data-dir /path/to/example/data
        provolone build example --snapshot-dir /path/to/example/snapshots
    """
    kwargs = {}
    if params:
        for kv in params:
            k, v = kv.split("=", 1)
            kwargs[k] = v

    # Pass data_dir and snapshot_dir as direct arguments
    df = _load(
        name,
        snapshot=snapshot,
        data_dir=data_dir,
        snapshot_dir=snapshot_dir,
        **kwargs,
    )  # type: ignore[arg-type]

    if head > 0:
        typer.echo(df.head(head).to_string())
    else:
        typer.echo(f"{name} built: shape={df.shape} cols={list(df.columns)[:6]}...")


@app.command()
def freeze(
    name: str,
    label: str = typer.Option(..., "--label", "-l", help="Snapshot label"),
    data_dir: Optional[str] = typer.Option(
        None,
        "--data-dir",
        help="Path to directory containing this dataset's data files",
    ),
    snapshot_dir: Optional[str] = typer.Option(
        None,
        "--snapshot-dir",
        help="Path to directory containing this dataset's snapshots",
    ),
    params: list[str] = typer.Option(None, help="key=val pairs"),
    force: bool = typer.Option(False, help="Overwrite snapshot data if exists"),
):
    """Create an immutable snapshot of a dataset.

    This command freezes a dataset at a specific point in time by creating
    a labeled snapshot. Snapshots are immutable by default and cannot be
    overwritten unless the --force flag is used.

    Examples:
        provolone freeze example --label 2024-01-15
        provolone freeze example --label prod-2024 --params vintage=2024
        provolone freeze example --label 2024-01-15 --force
        provolone freeze example --label prod --data-dir /path/to/example/data
        provolone freeze example --label prod --snapshot-dir /path/to/example/snapshots
    """
    kwargs = {}
    if params:
        for kv in params:
            k, v = kv.split("=", 1)
            kwargs[k] = v

    # Pass data_dir and snapshot_dir as direct arguments
    p = _freeze(
        name,
        snapshot=label,
        force=force,
        data_dir=data_dir,
        snapshot_dir=snapshot_dir,
        **kwargs,
    )
    typer.echo(f"Snapshot created at {p}")


@app.command("list")
def list_labels(
    name: str,
    snapshot_dir: Optional[str] = typer.Option(
        None, "--snapshot-dir", help="Custom snapshot directory"
    ),
):
    """List available snapshots for a dataset.

    Examples:
        provolone list example
        provolone list example --snapshot-dir /custom/path
    """
    from pathlib import Path

    custom_dir = Path(snapshot_dir) if snapshot_dir else None
    labs = list_snapshot_labels(name, snapshot_dir=custom_dir)
    typer.echo("\n".join(labs) if labs else "(none)")


@app.command()
def recreate(
    name: str,
    snapshot: str = typer.Option(
        ..., "--snapshot", "-s", help="Snapshot label to recreate from"
    ),
    snapshot_dir: Optional[str] = typer.Option(
        None,
        "--snapshot-dir",
        help="Path to directory containing this dataset's snapshots",
    ),
    output_dir: Optional[str] = typer.Option(
        None,
        "--output-dir",
        "-o",
        help="Output directory for recreated data",
    ),
    execute_potentially_unsafe: bool = typer.Option(
        False,
        "--execute-potentially-unsafe",
        help="Acknowledge security risk of executing code from snapshot recipe",
    ),
    params: list[str] = typer.Option(None, help="key=val pairs"),
):
    """Recreate a dataset from its snapshot recipe.

    This command rebuilds a dataset using only the captured source code stored
    in the snapshot metadata. It does not import any user modules, making the
    snapshot portable and reproducible even if the original code has changed.

    WARNING: This command executes code from the snapshot recipe. Only use
    snapshots from trusted sources. You must use --execute-potentially-unsafe
    to acknowledge this risk.

    Examples:
        provolone recreate example --snapshot 2024-01-15 --execute-potentially-unsafe
        provolone recreate example -s prod-2024 --execute-potentially-unsafe --params vintage=2024
        provolone recreate example -s v1 --execute-potentially-unsafe --output-dir /path/to/output
        provolone recreate example -s v1 --execute-potentially-unsafe --snapshot-dir /path/to/snapshots
    """
    kwargs = {}
    if params:
        for kv in params:
            k, v = kv.split("=", 1)
            kwargs[k] = v

    try:
        output_file = _recreate(
            name,
            snapshot=snapshot,
            snapshot_dir=snapshot_dir,
            output_dir=output_dir,
            execute_potentially_unsafe=execute_potentially_unsafe,
            **kwargs,
        )
        typer.echo("Dataset recreated successfully!")
        typer.echo(f"Output: {output_file}")
    except FileNotFoundError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except ValueError as e:
        typer.echo(f"Error: {e}", err=True)
        if "execute_potentially_unsafe" in str(e):
            typer.echo(
                "\nTo proceed, add the --execute-potentially-unsafe flag:", err=True
            )
            typer.echo(
                f"  provolone recreate {name} --snapshot {snapshot} --execute-potentially-unsafe",
                err=True,
            )
        else:
            typer.echo(
                "\nNote: Snapshots created before recipe support was added cannot be recreated.",
                err=True,
            )
            typer.echo("Please re-freeze the dataset to enable recreation.", err=True)
        raise typer.Exit(1)


@app.command()
def info(
    name: str,
    snapshot: Optional[str] = typer.Option(
        None, help="Label of snapshot to display info for"
    ),
    snapshot_dir: Optional[str] = typer.Option(
        None, "--snapshot-dir", help="Custom snapshot directory"
    ),
):
    """Display metadata information for a cached or snapshot dataset.

    This command shows comprehensive metadata about a dataset including shape,
    parameters, index information, file details, and raw file provenance.

    Examples:
        provolone info example
        provolone info example --snapshot 2024-01-15
        provolone info example --snapshot-dir /custom/path
    """
    from pathlib import Path
    from .snapshots import cache_path, snapshot_path, DEFAULT_SNAPSHOT_LABEL

    custom_dir = Path(snapshot_dir) if snapshot_dir else None

    # Determine which file to read
    if snapshot:
        file_path = snapshot_path(name, snapshot, snapshot_dir=custom_dir)
        label = snapshot
    else:
        file_path = cache_path(name, snapshot_dir=custom_dir)
        label = DEFAULT_SNAPSHOT_LABEL

    if not file_path.exists():
        if snapshot:
            typer.echo(
                f"Error: Snapshot '{snapshot}' for dataset '{name}' not found", err=True
            )
        else:
            typer.echo(
                f"Error: Cache for dataset '{name}' not found. Build it first with 'provolone build {name}'",
                err=True,
            )
        raise typer.Exit(1)

    try:
        # Read the metadata
        from .snapshots import read_df_from_path

        df, meta = read_df_from_path(file_path)

        # Display the metadata in a readable format
        typer.echo(f"Dataset: {name}")
        typer.echo(f"Label: {label}")
        typer.echo(f"Path: {file_path}")
        typer.echo()

        # Basic info
        if "shape" in meta:
            typer.echo(
                f"Shape: {meta['shape']['rows']} rows × {meta['shape']['cols']} columns"
            )
        else:
            typer.echo(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")

        # Parameters
        if meta.get("params"):
            typer.echo("\nParameters:")
            for k, v in meta["params"].items():
                typer.echo(f"  {k}: {v}")

        # Index info
        if "index" in meta or "fingerprint" in meta:
            index_info = meta.get("index") or meta.get("fingerprint")
            if index_info:
                typer.echo("\nIndex:")
                if "names" in index_info:
                    typer.echo(f"  Names: {index_info['names']}")
                if "dtypes" in index_info:
                    typer.echo(f"  Types: {index_info['dtypes']}")
                if "is_monotonic" in index_info:
                    typer.echo(f"  Monotonic: {index_info['is_monotonic']}")

        # File info
        if "file" in meta:
            typer.echo("\nFile Info:")
            if "bytes" in meta["file"]:
                size_mb = meta["file"]["bytes"] / (1024 * 1024)
                typer.echo(f"  Size: {size_mb:.2f} MB")
            if "sha256" in meta["file"]:
                typer.echo(f"  SHA256: {meta['file']['sha256'][:16]}...")

        # IO format
        if "io" in meta:
            typer.echo("\nFormat:")
            typer.echo(f"  Type: {meta['io'].get('format', 'unknown')}")
            typer.echo(f"  Compression: {meta['io'].get('compression', 'none')}")

        # Creation info
        if "created_at" in meta:
            typer.echo(f"\nCreated: {meta['created_at']}")

        if "version" in meta:
            typer.echo(f"Version: {meta['version']}")

        # Raw files metadata (if present)
        if "raw_files" in meta and meta["raw_files"]:
            typer.echo("\nRaw Files:")
            for idx, raw_file in enumerate(meta["raw_files"], 1):
                if len(meta["raw_files"]) > 1:
                    typer.echo(f"  File {idx}:")
                    prefix = "    "
                else:
                    prefix = "  "

                # Show file path
                if "file_at_load_path" in raw_file:
                    typer.echo(f"{prefix}Path: {raw_file['file_at_load_path']}")
                elif "raw_file_path" in raw_file:
                    typer.echo(f"{prefix}Path: {raw_file['raw_file_path']}")

                # Show URL if available
                if "raw_file_url" in raw_file:
                    typer.echo(f"{prefix}URL: {raw_file['raw_file_url']}")

                # Show source if available
                if "raw_file_source" in raw_file:
                    typer.echo(f"{prefix}Source: {raw_file['raw_file_source']}")

                # Show notes if available
                if "raw_file_notes" in raw_file:
                    typer.echo(f"{prefix}Notes: {raw_file['raw_file_notes']}")

                # Show SHA256 if available
                if "file_sha256" in raw_file:
                    typer.echo(f"{prefix}SHA256: {raw_file['file_sha256'][:16]}...")
                elif "raw_file_sha256" in raw_file:
                    typer.echo(f"{prefix}SHA256: {raw_file['raw_file_sha256'][:16]}...")

        # Content hash
        if "content_hash" in meta:
            typer.echo(f"\nContent Hash: {meta['content_hash'][:16]}...")

    except Exception as e:
        typer.echo(f"Error reading metadata: {e}", err=True)
        raise typer.Exit(1)


@app.command()
def tag(
    file_path: str,
    raw_file_url: Optional[str] = typer.Option(
        None, "--raw_file_url", help="URL where the file was obtained"
    ),
    raw_file_source: Optional[str] = typer.Option(
        None,
        "--raw_file_source",
        help="Data provider/source (e.g., 'Bureau of Labor Statistics')",
    ),
    raw_file_notes: Optional[str] = typer.Option(
        None, "--raw_file_notes", help="Notes about the file"
    ),
):
    """Tag a file with metadata, creating a sidecar .meta.json file.

    This command creates a metadata file alongside the specified data file
    to record provenance information such as URL, source, and notes. The metadata
    will be automatically used as defaults when loading datasets from this file.

    Examples:
        provolone tag data.csv --raw_file_url "https://example.com/data.csv"
        provolone tag data.csv --raw_file_source "Bureau of Labor Statistics"
        provolone tag data.csv --raw_file_notes "Downloaded on 2024-12-27"
    """
    kwargs = {}
    if raw_file_url:
        kwargs["raw_file_url"] = raw_file_url
    if raw_file_source:
        kwargs["raw_file_source"] = raw_file_source
    if raw_file_notes:
        kwargs["raw_file_notes"] = raw_file_notes

    meta_path = _tag(file_path, **kwargs)
    typer.echo(f"Metadata file created: {meta_path}")


@app.command()
def download(
    url: str,
    destination: Optional[str] = typer.Option(
        None, "--destination", "-d", help="Destination path for the downloaded file"
    ),
    source: Optional[str] = typer.Option(
        None,
        "--source",
        help="Data provider/source (e.g., 'Bureau of Labor Statistics')",
    ),
    notes: Optional[str] = typer.Option(
        None, "--notes", help="Notes about the download"
    ),
):
    """Download a file from a URL and automatically tag it with metadata.

    This command downloads a file from the specified URL and automatically
    creates a metadata sidecar file with the URL recorded as raw_file_url.

    Examples:
        provolone download https://example.com/data.csv
        provolone download https://example.com/data.csv --destination /path/to/file.csv
        provolone download https://example.com/data.csv --source "Bureau of Labor Statistics"
        provolone download https://example.com/data.csv --notes "Production data 2024"
    """
    file_path = _download(url, destination=destination, source=source, notes=notes)
    typer.echo(f"Downloaded to: {file_path}")
    typer.echo(f"Metadata file created: {file_path.with_suffix('.meta.json')}")


def main():
    app()


if __name__ == "__main__":
    main()
