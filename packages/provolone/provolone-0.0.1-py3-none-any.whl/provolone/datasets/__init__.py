from __future__ import annotations
from typing import Callable
import importlib.metadata as md


class DatasetRegistry(dict):
    """Registry for dataset classes.

    This class manages the registration and lookup of dataset classes.
    It extends dict to provide dataset-specific error handling.
    """

    def register(self, name: str, cls):
        """Register a dataset class.

        Args:
            name: Unique name for the dataset
            cls: Dataset class (must inherit from BaseDataset)

        Returns:
            The registered class (for use as decorator)

        Raises:
            ValueError: If dataset name is already registered
        """
        if name in self:
            raise ValueError(f"Dataset '{name}' already registered")
        self[name] = cls
        return cls


registry: DatasetRegistry = DatasetRegistry()


def register(name: str) -> Callable:
    """Decorator for registering dataset classes.

    Usage:
        @register("my_dataset")
        class MyDataset(BaseDataset):
            ...

    Args:
        name: Unique name for the dataset

    Returns:
        Decorator function
    """

    def deco(cls):
        return registry.register(name, cls)

    return deco


def get(name: str):
    """Get a dataset class by name.

    Args:
        name: Name of the dataset to retrieve

    Returns:
        Dataset class

    Raises:
        KeyError: If dataset name is not found
    """
    try:
        return registry[name]
    except KeyError:
        raise KeyError(
            f"Dataset '{name}' not found. "
            f"Installed plugins: {list(registry.keys()) or '(none)'}"
        )


def _load_plugins():
    """Load dataset plugins from entry points.

    This function discovers and loads all dataset plugins registered via
    the 'provolone.datasets' entry point group. Importing the entry points
    triggers plugin modules to call @register(...) to register their datasets.
    """
    # Importing entry points triggers plugin modules to call @register(...)
    for ep in md.entry_points(group="provolone.datasets"):
        try:
            ep.load()
        except Exception as e:
            import warnings

            warnings.warn(f"Failed to load dataset plugin '{ep.name}': {e}")


_load_plugins()

__all__ = ["DatasetRegistry", "registry", "register", "get"]
