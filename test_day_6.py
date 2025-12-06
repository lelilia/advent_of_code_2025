import pytest

from day_6 import part_1, part_2

with open("input6") as f:
    DATA = f.read()

with open("testinput6") as f:
    TEST_DATA = f.read()


@pytest.mark.parametrize(
    "data, exp",
    (
        (TEST_DATA, 4277556),
        (DATA, 5171061464548),
        (" 64 \n23 \n314\n+  ", 401),
        ("  51\n387\n215\n*  ", 4243455),
        (" 328\n64 \n98 \n+  ", 490),
        (" 123\n 45\n  6\n*  ", 33210),
    ),
)
def test_day_6_part_1(data, exp):
    assert (res := part_1(data)) == exp, f"Expected {exp}, got {res}"


@pytest.mark.parametrize(
    "data, exp",
    (
        (TEST_DATA, 3263827),
        # (DATA, 10189959087258),
        (" 64 \n 23 \n 314\n++  ", 1058),
        ("  51\n 387\n 215\n+*  ", 3253600),
        (" 328\n 64 \n 98 \n++  ", 625),
        (" 123\n  45\n   6\n+*  ", 8544),
    ),
)
def test_day_6_part_2(data, exp):
    assert (res := part_2(data)) == exp, f"Expected {exp}, got {res}"
