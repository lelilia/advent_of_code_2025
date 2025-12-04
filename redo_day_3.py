# second try
import time

INPUT = "input3"


def one_row(batteries, cnt_on):
    batteries = [int(x) for x in batteries]
    res_left = []
    res_right = []

    while (len_found := len(res_left) + len(res_right)) < cnt_on:
        index = batteries.index(max(batteries))
        if len_found + len(batteries[index:]) >= cnt_on:
            res_left = res_left + [batteries[index]]
            batteries = batteries[index + 1 :]
        else:
            res_right = batteries[index:] + res_right
            batteries = batteries[:index]
    return int("".join([str(x) for x in res_left + res_right]))


def solve(batteries, cnt_on):
    res = 0
    for line in batteries.split("\n"):
        res += one_row(line, cnt_on)
    return res


if __name__ == "__main__":
    t0 = time.time()
    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {solve(data, 2)}\t\t\t{(t1 := time.time()) - t0}s")
    print(f"Part 2: {solve(data, 12)}\t\t{time.time() - t1}s")
