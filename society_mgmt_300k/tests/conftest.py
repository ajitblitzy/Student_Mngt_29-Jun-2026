"""Shared pytest configuration for the society_mgmt suite.

Responsibilities
----------------
* **Import-path setup** — the importable package lives under ``src/`` (PyPA
  "src layout"). ``pyproject.toml`` already adds ``src`` to pytest's
  ``pythonpath``; this file makes the same guarantee explicitly so the suite
  also runs when invoked without that configuration (and without an editable
  install).
* **Single source of truth for the known-answer table** — the verified
  ``(input, expected)`` pairs are defined here once and injected into any test
  that declares ``x`` and ``expected`` parameters, and are also exposed through
  the ``known_answers`` fixture.
"""

import sys
from pathlib import Path

import pytest

# Make ``import society_mgmt`` resolve to the in-tree src/ package.
_SRC = Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

# Known-answer pairs verified against the original JavaScript corpus and the
# README behaviour table. compute(x) == 6*x, plus 10 when that result is even.
KNOWN_ANSWERS = [
    (0, 10),
    (1, 16),
    (2, 22),
    (3, 28),
    (5, 40),
    (10, 70),
    (-4, -14),
    (2.5, 15.0),
]


def pytest_generate_tests(metafunc):
    """Auto-parametrize any test that declares both ``x`` and ``expected``."""
    if {"x", "expected"} <= set(metafunc.fixturenames):
        metafunc.parametrize("x,expected", KNOWN_ANSWERS)


@pytest.fixture
def known_answers():
    """Return the verified ``(input, expected)`` known-answer pairs."""
    return list(KNOWN_ANSWERS)
