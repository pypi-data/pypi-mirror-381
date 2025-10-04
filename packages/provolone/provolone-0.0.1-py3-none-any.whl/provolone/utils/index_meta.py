from __future__ import annotations
import json
from typing import Any, List, Dict
import pandas as pd
import numpy as np
import datetime as dt
from pandas.api.types import CategoricalDtype


def _names(idx: pd.Index) -> List[str | None]:
    """Extract index names from pandas Index or MultiIndex.

    Args:
        idx: pandas Index or MultiIndex

    Returns:
        List of index names (None for unnamed indices)
    """
    return list(idx.names) if isinstance(idx, pd.MultiIndex) else [idx.name]


def _dtypes(idx: pd.Index) -> List[str]:
    """Extract data types from pandas Index or MultiIndex.

    Args:
        idx: pandas Index or MultiIndex

    Returns:
        List of string representations of dtypes
    """
    if isinstance(idx, pd.MultiIndex):
        return [
            str(level.dtype) if hasattr(level, "dtype") else "object"
            for level in idx.levels
        ]
    return [str(getattr(idx, "dtype", "object"))]


def _tz(idx: pd.Index) -> List[str | None]:
    """Extract timezone information from pandas Index or MultiIndex.

    Args:
        idx: pandas Index or MultiIndex

    Returns:
        List of timezone strings (None for non-timezone-aware indices)
    """

    def tz_of(x):
        try:
            tz = getattr(x, "tz", None)
            return str(tz) if tz else None
        except Exception:
            return None

    if isinstance(idx, pd.MultiIndex):
        return [tz_of(level) for level in idx.levels]
    return [tz_of(idx)]


def _to_jsonable(x: Any) -> Any:
    """Convert pandas/numpy objects to JSON-serializable primitives.

    Args:
        x: Object to convert

    Returns:
        JSON-serializable representation of the object
    """
    # Convert objects to JSON-serializable primitives
    if isinstance(x, pd.Timestamp):
        return x.isoformat()
    if isinstance(x, (dt.datetime, dt.date, dt.time)):
        return x.isoformat()
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.floating,)):
        return float(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, (np.ndarray,)):
        return [_to_jsonable(v) for v in x.tolist()]
    return x


def _jsonify_sample(sample: Any) -> Any:
    """Recursively convert sample data to JSON-serializable format.

    Args:
        sample: Sample data (can be nested lists/tuples)

    Returns:
        JSON-serializable version of the sample data
    """
    if isinstance(sample, (list, tuple)):
        return [_jsonify_sample(v) for v in sample]
    return _to_jsonable(sample)


def index_fingerprint(idx: pd.Index) -> Dict[str, Any]:
    """Create a comprehensive fingerprint of a pandas Index.

    This function captures metadata about the index structure, data types,
    and a small sample of data for comparison and debugging purposes.

    Args:
        idx: pandas Index or MultiIndex

    Returns:
        Dict containing index metadata including names, dtypes, timezone info,
        monotonicity, categorical flags, and a data sample
    """
    if isinstance(idx, pd.MultiIndex):
        raw_sample = [lvl[:3].tolist() for lvl in idx.levels]
        cat = [isinstance(lvl.dtype, CategoricalDtype) for lvl in idx.levels]
    else:
        raw_sample = idx[:3].tolist()
        cat = [isinstance(idx.dtype, CategoricalDtype)]
    sample = _jsonify_sample(raw_sample)
    return {
        "names": _names(idx),
        "dtypes": _dtypes(idx),
        "tz": _tz(idx),
        "is_monotonic": bool(idx.is_monotonic_increasing),
        "categorical": cat,
        "sample": sample,
    }


def write_index_meta(base_path: str, idx: pd.Index) -> None:
    """Write index metadata to a JSON sidecar file.

    Creates a .meta.json file alongside the data file containing comprehensive
    index metadata including backward-compatible index_cols field.

    Args:
        base_path: Base path for the data file (without extension)
        idx: pandas Index or MultiIndex to capture metadata for
    """
    meta = {
        "index_cols": _names(idx),  # backward compatible
        "fingerprint": index_fingerprint(idx),
    }
    with open(base_path + ".meta.json", "w") as f:
        json.dump(meta, f, indent=2)


def read_index_meta(base_path: str) -> dict | None:
    """Read index metadata from a JSON sidecar file.

    Args:
        base_path: Base path for the data file (without extension)

    Returns:
        Dict containing index metadata, or None if file doesn't exist
    """
    try:
        with open(base_path + ".meta.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
