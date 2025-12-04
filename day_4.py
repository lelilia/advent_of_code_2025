# Advent of Code 2025 - Day 4

import time

INPUT = "input4"
# INPUT = "testinput4"

NEIGBORS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def part_1(data):
    res = 0
    map = [[x for x in line] for line in data.split("\n")]
    for x, row in enumerate(map):
        for y, cell in enumerate(row):
            if cell == "@":
                cnt = 0
                for (dx, dy) in NEIGBORS:
                    if 0 <= x + dx < len(map) and 0 <= y + dy < len(map[0]):
                        if map[x + dx][y + dy] == "@":
                            cnt += 1
                if cnt < 4:
                    res += 1
    return res


def part_2(data):
    res = 0
    map = [[x for x in line] for line in data.split("\n")]
    to_remove = [1]
    while len(to_remove) > 0:
        to_remove = []
        for x, row in enumerate(map):
            for y, cell in enumerate(row):
                if cell == "@":
                    cnt = 0
                    for (dx, dy) in NEIGBORS:
                        if 0 <= x + dx < len(map) and 0 <= y + dy < len(map[0]):
                            if map[x + dx][y + dy] == "@":
                                cnt += 1
                    if cnt < 4:
                        res += 1

                        to_remove.append((x, y))
        for x, y in to_remove:

            map[x][y] = "."
    return res


if __name__ == "__main__":
    t0 = time.time()
    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}         {time.time() - t0}s")
    print(f"Part 2: {part_2(data)}         {time.time() - t0}s")
