from __future__ import annotations
from pathlib import Path
import hashlib
import pandas as pd


def _hash_bytes(data: bytes) -> str:
    """Generate a short SHA-256 hash of byte data.

    Args:
        data: Input bytes to hash

    Returns:
        First 16 characters of SHA-256 hexdigest
    """
    return hashlib.sha256(data).hexdigest()[:16]


def hash_file(path: Path, truncate: bool = True) -> str:
    """Calculate SHA-256 hash of a file (streamed for large files).

    Args:
        path: Path to the file to hash
        truncate: If True, return first 16 characters; if False, return full hash

    Returns:
        SHA-256 hexdigest (truncated to 16 chars by default for backward compatibility)
    """
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    digest = h.hexdigest()
    return digest[:16] if truncate else digest


def hash_df(df: pd.DataFrame) -> str:
    """
    Stable content hash for a pandas DataFrame.
    Uses pandas.util.hash_pandas_object on index and columns,
    and incorporates column dtypes to avoid dtype-related collisions.
    Returns a short (16 hex chars) SHA-256 digest.
    """
    from pandas.util import hash_pandas_object

    # Hash the index (including name/levels)
    h_index = hash_pandas_object(df.index, index=True).values

    parts = [h_index.tobytes()]
    for col in df.columns:
        col_hash = hash_pandas_object(df[col], index=False).values.tobytes()
        dtype_sig = str(df[col].dtype).encode("utf-8")
        parts.append((col if isinstance(col, str) else str(col)).encode("utf-8"))
        parts.append(dtype_sig)
        parts.append(col_hash)

    return _hash_bytes(b"".join(parts))
