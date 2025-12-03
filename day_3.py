# Advent of Code -- Day 3

import time

INPUT = "input3"
# INPUT = "testinput3"


def get_number_of_free_spaces(batteries, switched_on, index):
    return len(
        [x for i, x in enumerate(batteries[index:]) if not switched_on[index + i]]
    )


def switch(batteries, number_batteries_on):
    batteries = [int(x) for x in batteries]
    switched_on = [False] * len(batteries)
    bats = batteries.copy()
    start_index = 0

    while sum(switched_on) < number_batteries_on:
        max_value = max(bats[start_index:])
        max_index = bats[start_index:].index(max_value) + start_index
        switched_on[max_index] = True
        rest_length = get_number_of_free_spaces(
            batteries=batteries, switched_on=switched_on, index=max_index
        )
        needed_length = number_batteries_on - sum(switched_on)
        if rest_length <= needed_length:
            switched_on = [
                x if i < max_index else True for i, x in enumerate(switched_on)
            ]
            bats = [x if i < max_index else -100 for i, x in enumerate(bats)]
        elif rest_length > needed_length:
            start_index = max_index + 1
    res = int("".join([str(x) for i, x in enumerate(batteries) if switched_on[i]]))
    return res


def solve(data, number_of_batteries=2):
    summe = 0
    for batteries in data:
        batteries = batteries.strip("\n")

        summe += switch(batteries, number_of_batteries)

    return summe


if __name__ == "__main__":
    t0 = time.time()
    with open(INPUT) as f:
        data = f.readlines()

    print(f"Part 1: {solve(data)}        {time.time() - t0}")
    print(f"Part 2: {solve(data, 12)}     {time.time() - t0}")

    with open("testinput3") as f:
        test_data = f.readlines()

    assert solve(test_data, 12) == 3121910778619
