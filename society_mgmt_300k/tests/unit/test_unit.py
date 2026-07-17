import pytest

from society_mgmt import compute


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 10),
        (1, 16),
        (2, 22),
        (3, 28),
        (5, 40),
        (10, 70),
        (-4, -14),
        (2.5, 15.0),
    ],
)
def test_compute_known_answers(x, expected):
    assert compute(x) == expected
