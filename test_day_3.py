import pytest
from day_3 import switch, get_number_of_free_spaces


def test_switch():
    batteries = "987654321111111"
    res = switch(batteries, 2)
    exp = 98
    assert res == exp


def test_switch2():
    batteries = "987654321111111"
    res = switch(batteries, 12)
    exp = 987654321111
    assert res == exp


def test_switch3():
    batteries = "811111111111119"
    res = switch(batteries, 2)
    exp = 89
    assert res == exp


def test_switch4():
    batteries = "811111111111119"
    res = switch(batteries, 12)
    exp = 811111111119
    assert res == exp


def test_switch5():
    batteries = "234234234234278"
    res = switch(batteries, 2)
    exp = 78
    assert res == exp


def test_switch6():
    batteries = "234234234234278"
    res = switch(batteries, 12)
    exp = 434234234278
    assert res == exp


def test_switch7():
    batteries = "3322343713826221125922247222221263232222632332333222231223221432225352522227622122311323531262273513"
    res = switch(batteries, 12)
    exp = 977662273513
    assert res == exp


def test_switch8():
    batteries = "5533541345563534455432555454434414411366573335634663523353143544535254433516534123415359511733347333"
    res = switch(batteries, 12)
    exp = 951733347333
    assert res == exp


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
