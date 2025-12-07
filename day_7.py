# Advent of Code 2025 - day 7

import time

import numpy as np

INPUT = "input7"
# INPUT = "testinput7"


def get_diagram(data):
    s_pos = data.index("S")
    diagram = np.array(
        [[0 if char == "." else 1 for char in line] for line in data.split("\n")]
    )
    return diagram, s_pos


def part_1(data):
    diagram, s_pos = get_diagram(data)

    beam = {s_pos}
    cnt_split = 0

    for row in range(1, diagram.shape[0]):
        new_beam = set()
        for b in beam:
            if diagram[row, b] == 1:
                new_beam.add(b - 1)
                new_beam.add(b + 1)
                cnt_split += 1
            else:
                new_beam.add(b)
        beam = new_beam

    return cnt_split


def part_2(data):
    diagram, s_pos = get_diagram(data)
    beam = {s_pos: 1}

    for row in range(1, diagram.shape[0]):
        new_beam = {x: 0 for x in range(diagram.shape[1])}
        for b in beam:
            if beam[b] == 0:
                continue
            if diagram[row, b] == 1:
                new_beam[b + 1] += beam[b]
                new_beam[b - 1] += beam[b]

            else:
                new_beam[b] += beam[b]
        beam = new_beam

    return sum(beam.values())


if __name__ == "__main__":
    t0 = time.time()

    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}\t\t\t{-t0 + (t1 := time.time())}s")
    print(f"Part 2: {part_2(data)}\t\t{-t1 + time.time()}s")
