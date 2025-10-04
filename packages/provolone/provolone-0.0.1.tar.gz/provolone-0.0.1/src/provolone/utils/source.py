"""Utilities for extracting and normalizing method source code."""

from __future__ import annotations
import inspect
import textwrap
import hashlib
from typing import Any, Callable


def extract_method_source(method: Callable) -> str | None:
    """Extract the source code of a method and normalize it.

    Args:
        method: The method to extract source from

    Returns:
        Normalized source code string, or None if source cannot be extracted
    """
    try:
        # Get the source code
        source = inspect.getsource(method)

        # Dedent to remove class indentation
        source = textwrap.dedent(source)

        # Remove leading/trailing whitespace
        source = source.strip()

        return source
    except (OSError, TypeError):
        # Can't get source (e.g., built-in method, C extension)
        return None


def hash_source(source: str) -> str:
    """Generate a hash of source code.

    Args:
        source: Source code string

    Returns:
        Hexadecimal hash string (first 16 characters of SHA256)
    """
    return hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]


def extract_method_recipe(obj: Any, method_name: str) -> dict | None:
    """Extract source code and hash for a method.

    Args:
        obj: Object containing the method
        method_name: Name of the method to extract

    Returns:
        Dictionary with 'source' and 'hash' keys, or None if method doesn't exist
        or source cannot be extracted
    """
    if not hasattr(obj, method_name):
        return None

    method = getattr(obj, method_name)
    source = extract_method_source(method)

    if source is None:
        return None

    return {
        "source": source,
        "hash": hash_source(source),
    }
