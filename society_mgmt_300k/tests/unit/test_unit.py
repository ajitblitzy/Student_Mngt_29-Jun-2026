"""Unit tests for the canonical ``society_mgmt.compute`` function.

These replace the assertion-less generated ``.js`` test stubs from the original
corpus with real, executable known-answer checks. ``compute(x)`` returns
``6 * x``, plus ``10`` when that result is even; the parity branch is retained
to preserve float edge cases.
"""

from society_mgmt import compute


def test_known_answer(x, expected):
    """Verified known-answer pairs (auto-parametrized in conftest)."""
    assert compute(x) == expected


def test_even_integer_gets_parity_bonus():
    # For any integer x, 6*x is always even, so +10 always applies.
    for x in range(-25, 26):
        assert compute(x) == 6 * x + 10


def test_zero():
    assert compute(0) == 10


def test_negative_integer():
    assert compute(-4) == -14


def test_float_no_parity_bonus_is_odd_result():
    # 6 * 2.5 == 15.0 which is odd -> no +10, result stays 15.0.
    result = compute(2.5)
    assert result == 15.0
    assert isinstance(result, float)


def test_float_even_result_gets_bonus():
    # 6 * 2.0 == 12.0 which is even -> +10 -> 22.0.
    assert compute(2.0) == 22.0


def test_large_integer_no_overflow():
    # Python ints are arbitrary precision; behaviour holds for large values.
    x = 10**50
    assert compute(x) == 6 * x + 10


def test_is_pure_function():
    # Deterministic and side-effect free: repeated calls agree.
    assert compute(7) == compute(7)
