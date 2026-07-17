import importlib

import pytest

from society_mgmt import compute

LAYERS = [
    "config",
    "controllers",
    "domain",
    "middleware",
    "models",
    "repositories",
    "routes",
    "services",
    "utils",
]


@pytest.mark.parametrize("layer", LAYERS)
def test_layer_reexports_compute(layer):
    module = importlib.import_module(f"society_mgmt.{layer}")
    assert module.compute is compute
    assert module.compute(2) == 22
