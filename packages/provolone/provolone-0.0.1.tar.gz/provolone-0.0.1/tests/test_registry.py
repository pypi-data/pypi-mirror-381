def test_registry_has_example():
    from provolone import registry

    # Ensure the example dataset is registered
    assert "example" in registry
