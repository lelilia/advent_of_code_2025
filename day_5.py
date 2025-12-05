# Advent of Code 2025 - day 5
import time
INPUT = "input5"
# INPUT = "testinput5"

def test_id(id, ranges):
    for start, stop in ranges:
        if start <= id <= stop:
            return 1
    return 0

def part_1(data):
    ranges, ids = data.split("\n\n")
    ranges = [[int(x) for x in line.split("-")] for line in ranges.split("\n")]
    ids = [int(x) for x in ids.split("\n")]
    res = 0
    for id in ids:
        res += test_id(id, ranges)
    return res


def part_2(data):
    ranges, _ = data.split("\n\n")
    q = [[int(x) for x in line.split("-")] for line in ranges.split("\n")]
    q = sorted(q, key=lambda x: x[0])

    res = 0
    (x,y) = q.pop(0)
    while q:
        (x1, y1) = q.pop(0)
        if x > y1+1  or y+1 < x1:
            res += y + 1 - x
            x, y = x1, y1
        else:
            x = min([x,x1])
            y = max([y,y1])
    res += y + 1 - x

    return res


if __name__ == "__main__":

    t0 = time.time()
    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}\t\t\t{-t0 + (t1 := time.time())}")
    print(f"Part 2: {part_2(data)}\t\t{-t1 + time.time()}")