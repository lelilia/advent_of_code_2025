import pytest
from day_3 import switch_batteries_on, get_number_of_free_spaces


@pytest.mark.parametrize(
    "batteries, cnt_on, expected",
    (
        ("987654321111111", 2, 98),
        ("987654321111111", 12, 987654321111),
        ("811111111111119", 2, 89),
        ("811111111111119", 12, 811111111119),
        ("234234234234278", 2, 78),
        ("234234234234278", 12, 434234234278),
        ("3322343713826221125922247222221263232222632332333222231223221432225352522227622122311323531262273513", 2, 97),
        ("3322343713826221125922247222221263232222632332333222231223221432225352522227622122311323531262273513", 12, 977662273513)
    ),
)
def test_par(batteries, cnt_on, expected):
    assert ( res := switch_batteries_on(batteries, cnt_on)) == expected, f"Expected {expected}, got {res} for {batteries}"







def test_number_of_free_spaces():
    batteries = [int(x) for x in "342944278"]
    switched_on = [False, False, False, True, False, False, False, True, True]
    index = 3
    res = get_number_of_free_spaces(
        batteries=batteries, switched_on=switched_on, index=index
    )
    exp = 3
    assert res == exp


def test_number_of_free_spaces2():
    batteries = [int(x) for x in "342944278"]
    switched_on = [False, False, False, True, True, False, False, True, True]
    index = 4
    res = get_number_of_free_spaces(
        batteries=batteries, switched_on=switched_on, index=index
    )
    exp = 2
    assert res == exp
