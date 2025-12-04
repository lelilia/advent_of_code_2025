import pytest
from redo_day_4 import solve, brute_force, with_dict, second_try, with_numpy

DATA = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


@pytest.mark.parametrize(
    "input, part, method, expected",
    (
        (DATA, 1, brute_force, 13),
        (DATA, 2, brute_force, 43),
        (DATA, 1, with_dict, 13),
        (DATA, 2, with_dict, 43),
        (DATA, 1, second_try, 13),
        (DATA, 2, second_try, 43),
        (DATA, 1, with_numpy, 13),
        (DATA, 2, with_numpy, 43),
    ),
)
def test_solve(input, part, method, expected):
    assert (
        res := solve(input, part, method)
    ) == expected, f"Expected {expected}, got {res} for {method}"
