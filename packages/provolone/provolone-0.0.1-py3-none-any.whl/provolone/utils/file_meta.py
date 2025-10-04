"""File metadata extraction utilities."""

from __future__ import annotations
from pathlib import Path
import datetime as dt
from typing import Optional
from .hash import hash_file


def extract_file_metadata_for_tagging(
    raw_path: Path, url: Optional[str] = None, source: Optional[str] = None, notes: Optional[str] = None
) -> dict:
    """Extract metadata for tagging (sidecar creation) - uses old format.
    
    This function creates metadata in the original format that will be used
    as the canonical provenance record when copying files.
    
    Args:
        raw_path: Path to the raw file
        url: User-provided URL where the file was obtained
        source: User-provided data provider/source (e.g., "Bureau of Labor Statistics")
        notes: User-provided notes about the file/source

    Returns:
        Dictionary containing file metadata fields in original format
    """
    path = Path(raw_path)

    # Basic file information
    file_meta = {
        "raw_file_path": str(path.absolute()),
        "raw_file_name": path.name,
        "raw_file_exists": path.exists(),
    }

    # Add user-provided fields if available
    if url is not None:
        file_meta["raw_file_url"] = url
    if source is not None:
        file_meta["raw_file_source"] = source
    if notes is not None:
        file_meta["raw_file_notes"] = notes

    # Only extract file properties if file exists
    if path.exists():
        try:
            stat = path.stat()
            file_meta["raw_file_size"] = stat.st_size

            # Convert mtime to ISO8601 string
            mtime = dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc)
            file_meta["raw_file_mtime"] = mtime.isoformat()

            # Calculate SHA256 hash (full hash for metadata)
            file_meta["raw_file_sha256"] = hash_file(path, truncate=False)

            # File extension as file type
            if path.suffix:
                file_meta["raw_file_type"] = path.suffix.lstrip(".")

        except (OSError, PermissionError) as e:
            # If we can't read file stats, record the error
            file_meta["raw_file_error"] = str(e)

    return file_meta


def extract_file_metadata(
    raw_path: Path, url: Optional[str] = None, source: Optional[str] = None, notes: Optional[str] = None, 
    sidecar_meta: Optional[dict] = None
) -> dict:
    """Extract comprehensive metadata from a file path.

    Args:
        raw_path: Path to the raw file
        url: User-provided URL where the file was obtained
        source: User-provided data provider/source (e.g., "Bureau of Labor Statistics")
        notes: User-provided notes about the file/source
        sidecar_meta: Optional sidecar metadata to compare against

    Returns:
        Dictionary containing file metadata fields
    """
    path = Path(raw_path)

    # Start with basic file information at load time
    file_meta = {
        "file_at_load_path": str(path.absolute()),
        "file_at_load_name": path.name,
        "file_at_load_exists": path.exists(),
    }

    # Only extract file properties if file exists
    if path.exists():
        try:
            stat = path.stat()
            file_meta["file_at_load_size"] = stat.st_size

            # Convert mtime to ISO8601 string
            mtime = dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc)
            file_meta["file_at_load_mtime"] = mtime.isoformat()

            # Calculate SHA256 hash (full hash for metadata)
            current_sha256 = hash_file(path, truncate=False)
            file_meta["file_at_load_sha256"] = current_sha256

            # File extension as file type
            if path.suffix:
                file_meta["file_at_load_type"] = path.suffix.lstrip(".")

            # Check if we have sidecar metadata and if SHA256 matches
            sha256_match = False
            if sidecar_meta and "raw_file_sha256" in sidecar_meta:
                sidecar_sha256 = sidecar_meta["raw_file_sha256"]
                sha256_match = current_sha256 == sidecar_sha256
                file_meta["raw_file_sidecar_sha256"] = sidecar_sha256

            file_meta["raw_file_sha256_match"] = sha256_match

            if sha256_match:
                # SHA256 matches - preserve all raw_file_* fields from sidecar
                if sidecar_meta:
                    for key, value in sidecar_meta.items():
                        if key.startswith("raw_file_"):
                            file_meta[key] = value
                
                # Override with user-provided values if specified
                if url is not None:
                    file_meta["raw_file_url"] = url
                if source is not None:
                    file_meta["raw_file_source"] = source
                if notes is not None:
                    file_meta["raw_file_notes"] = notes
            else:
                # SHA256 doesn't match or no sidecar - recompute raw_file_* fields
                file_meta["raw_file_path"] = str(path.absolute())
                file_meta["raw_file_name"] = path.name
                file_meta["raw_file_exists"] = path.exists()
                file_meta["raw_file_size"] = stat.st_size
                file_meta["raw_file_mtime"] = mtime.isoformat()
                file_meta["raw_file_sha256"] = current_sha256

                # File extension as file type
                if path.suffix:
                    file_meta["raw_file_type"] = path.suffix.lstrip(".")

                # Add user-provided fields if available
                if url is not None:
                    file_meta["raw_file_url"] = url
                if source is not None:
                    file_meta["raw_file_source"] = source
                if notes is not None:
                    file_meta["raw_file_notes"] = notes

        except (OSError, PermissionError) as e:
            # If we can't read file stats, record the error
            file_meta["file_at_load_error"] = str(e)
            file_meta["raw_file_error"] = str(e)
    else:
        # File doesn't exist - set basic raw_file_* fields
        file_meta["raw_file_path"] = str(path.absolute())
        file_meta["raw_file_name"] = path.name
        file_meta["raw_file_exists"] = False
        file_meta["raw_file_sha256_match"] = False
        
        # Add user-provided fields if available
        if url is not None:
            file_meta["raw_file_url"] = url
        if source is not None:
            file_meta["raw_file_source"] = source
        if notes is not None:
            file_meta["raw_file_notes"] = notes

    return file_meta
