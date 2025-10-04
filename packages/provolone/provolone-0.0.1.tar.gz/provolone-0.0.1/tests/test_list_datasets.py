def test_list_datasets():
    """Test the list_datasets() convenience function."""
    import provolone

    # Ensure the example dataset is loaded

    # Test the convenience function
    datasets = provolone.list_datasets()
    assert isinstance(datasets, list)
    assert "example" in datasets

    # Verify it matches the registry directly
    from provolone.datasets import registry

    assert datasets == list(registry.keys())


def test_list_datasets_empty_registry():
    """Test list_datasets() with empty registry."""
    import provolone
    from provolone.datasets import DatasetRegistry

    # Create a fresh registry instance for testing
    old_registry = provolone.registry
    try:
        # Temporarily replace with empty registry
        provolone.registry = DatasetRegistry()

        datasets = provolone.list_datasets()
        assert isinstance(datasets, list)
        assert len(datasets) == 0
    finally:
        # Restore original registry
        provolone.registry = old_registry
