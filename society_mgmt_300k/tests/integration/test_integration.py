"""Integration tests: cross-package imports over the nine layer subpackages.

The original corpus preserved a nine-namespace taxonomy (config, controllers,
domain, middleware, models, repositories, routes, services, utils). In the
migrated package each namespace is a thin subpackage that re-exports the single
canonical ``compute``. These tests assert that structural contract: every layer
resolves to the *same* function object and produces identical results.
"""

import importlib

import pytest

import society_mgmt

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


def test_top_level_exports_compute():
    assert hasattr(society_mgmt, "compute")
    assert callable(society_mgmt.compute)


@pytest.mark.parametrize("layer", LAYERS)
def test_layer_reexports_same_compute(layer):
    module = importlib.import_module(f"society_mgmt.{layer}")
    assert hasattr(module, "compute"), f"{layer} must re-export compute"
    # Every layer must delegate to the one canonical function object.
    assert module.compute is society_mgmt.compute


@pytest.mark.parametrize("layer", LAYERS)
def test_layer_matches_known_answers(layer, known_answers):
    module = importlib.import_module(f"society_mgmt.{layer}")
    for x, expected in known_answers:
        assert module.compute(x) == expected


def test_all_layers_agree_across_domain(known_answers):
    modules = [importlib.import_module(f"society_mgmt.{layer}") for layer in LAYERS]
    for x, _ in known_answers:
        results = {society_mgmt.compute(x)} | {m.compute(x) for m in modules}
        assert len(results) == 1, f"layers disagreed for x={x}: {results}"
