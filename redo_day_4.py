# Advent of Code 2025 - Day 4

import time
import numpy as np


INPUT = "input4"
# INPUT = "testinput4.txt"
NEIGBORS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def load_diagram(data, pad=True):
    diagram = np.array(
        [[0 if x == "." else 1 for x in row] for row in data.split("\n")]
    )
    if pad:
        diagram = np.pad(diagram, 1, constant_values=0)
    return diagram


def numpy_part_1(data):
    diagram = load_diagram(data)
    n, m = diagram.shape
    res = np.array(
        [
            [
                1
                if np.sum(diagram[x - 1 : x + 2, y - 1 : y + 2]) < 5
                and diagram[x, y] == 1
                else 0
                for y in range(1, m - 1)
            ]
            for x in range(1, n - 1)
        ]
    )
    return np.sum(res)


def numpy_part_2(data):

    diagram = load_diagram(data)
    n, m = diagram.shape
    cnt_moved = 1
    cnt_total = 0
    while cnt_moved > 0:
        moveable = np.array(
            [
                [
                    1
                    if np.sum(diagram[x - 1 : x + 2, y - 1 : y + 2]) < 5
                    and diagram[x, y] == 1
                    else 0
                    for y in range(1, m - 1)
                ]
                for x in range(1, n - 1)
            ]
        )
        cnt_total += (cnt_moved := np.sum(moveable))
        moveable = np.pad(moveable, 1, constant_values=0)
        diagram = diagram - moveable

    return cnt_total


def with_numpy(data, part):
    if part == 1:
        return numpy_part_1(data)
    return numpy_part_2(data)


def with_dict_part_1(data):
    row_length = data.index("\n") + 1
    boxes = {
        (i % row_length, i // row_length): 1
        for i, char in enumerate(data)
        if char == "@"
    }
    cnt_moved = 0
    for x, y in boxes:
        cnt_neigbors = 0
        for dx, dy in NEIGBORS:
            cnt_neigbors += boxes.get((x + dx, y + dy), 0)
        if cnt_neigbors < 4:
            cnt_moved += 1

    return cnt_moved


def with_dict_part_2(data):
    row_length = data.index("\n") + 1
    boxes = {
        (i % row_length, i // row_length): 1
        for i, char in enumerate(data)
        if char == "@"
    }
    cnt_moved = 0
    moveable = [0]
    while len(moveable) > 0:
        moveable = []
        for x, y in boxes:
            cnt_neigbors = 0
            for dx, dy in NEIGBORS:
                cnt_neigbors += boxes.get((x + dx, y + dy), 0)
            if cnt_neigbors < 4:
                cnt_moved += 1
                moveable.append((x, y))
        for box in moveable:
            del boxes[box]

    return cnt_moved


def with_dict(data, part):
    if part == 1:
        return with_dict_part_1(data)
    return with_dict_part_2(data)


def brute_force(data, part):
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
        if part == 1:
            return res
        for x, y in to_remove:

            map[x][y] = "."
    return res


def snd_try_part_1(data):
    cnt_moved = 0
    diagram = [[1 if x == "@" else 0 for x in line] for line in data.split("\n")]
    max_x, max_y = len(diagram), len(diagram[0])
    for x, row in enumerate(diagram):
        for y, cell in enumerate(row):
            cnt_boxes = 0
            if cell == 1:
                for dx, dy in NEIGBORS:
                    if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                        cnt_boxes += diagram[x + dx][y + dy]
                if cnt_boxes < 4:
                    cnt_moved += 1
    return cnt_moved


def snd_try_part_2(data):
    cnt_moved = 0
    diagram = [[1 if x == "@" else 0 for x in line] for line in data.split("\n")]
    max_x, max_y = len(diagram), len(diagram[0])
    moveable = [0]
    while len(moveable) > 0:
        moveable = []
        for x, row in enumerate(diagram):
            for y, cell in enumerate(row):
                cnt_boxes = 0
                if cell == 1:
                    for dx, dy in NEIGBORS:
                        if 0 <= x + dx < max_x and 0 <= y + dy < max_y:
                            cnt_boxes += diagram[x + dx][y + dy]
                    if cnt_boxes < 4:
                        moveable.append((x, y))
        for x, y in moveable:
            cnt_moved += 1
            diagram[x][y] = 0

    return cnt_moved


def second_try(data, part):
    if part == 1:
        return snd_try_part_1(data)
    return snd_try_part_2(data)


def solve(data, part=1, method=brute_force):
    return method(data, part)


if __name__ == "__main__":
    t0 = time.time()
    with open(INPUT) as f:
        data = f.read()

    print(
        f"Part 1 - with_dict:   {solve(data, 1, with_dict)}\t\t{-t0 + (t1 := time.time())}s"
    )
    print(
        f"Part 2 - with_dict:   {solve(data, 2, with_dict)}\t\t{-t1 + (t2 := time.time())}s"
    )
    print()
    print(
        f"Part 1 - brute_force: {solve(data, 1, brute_force)}\t\t{-t2 + (t3 := time.time())}s"
    )
    print(
        f"Part 2 - brute_force: {solve(data, 2, brute_force)}\t\t{-t3 + (t4 := time.time())}s"
    )
    print()
    print(
        f"Part 1 - second_try:  {solve(data, 1, second_try)}\t\t{-t4 + (t5 := time.time())}s"
    )
    print(
        f"Part 2 - second_try:  {solve(data, 2, second_try)}\t\t{-t5 + (t6 := time.time())}s"
    )
    print()
    print(
        f"Part 1 - with_numpy:  {solve(data, 1, with_numpy)}\t\t{-t6 + (t7 := time.time())}s"
    )
    print(
        f"Part 2 - with_numpy:  {solve(data, 2, with_numpy)}\t\t{-t7 + (t8 := time.time())}s"
    )
