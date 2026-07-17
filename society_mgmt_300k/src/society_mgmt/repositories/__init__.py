"""society_mgmt.repositories: thin namespace layer preserved from the original
corpus taxonomy. It re-exports the single canonical :func:`compute` so that
``from society_mgmt.repositories import compute`` resolves to the same function as
``from society_mgmt import compute``.
"""

from society_mgmt.core import compute

__all__ = ["compute"]
