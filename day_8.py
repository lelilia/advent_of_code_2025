# Advent of Code 2025 - day 8

import time
from math import prod, sqrt

INPUT = "input8"
TIMES = 1000

# INPUT = "testinput8"
# TIMES = 10


class List:
    def __init__(self, name):
        self.name = name


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def part_1(data, times=TIMES):
    data = [
        (i, [int(number) for number in line.split(",")])
        for i, line in enumerate(data.split("\n"))
    ]

    distances = []
    for i in range(len(data) - 1):
        index_1, p1 = data[i]
        for j in range(i + 1, len(data)):
            index_2, p2 = data[j]
            distances.append((distance(p1, p2), index_1, index_2))
    distances = sorted(distances, key=lambda x: x[0])

    lists = []
    for _ in range(times):
        # see if the point are already in a list
        _, point_1, point_2 = distances.pop(0)
        index_1 = index_2 = None
        for index, l in enumerate(lists):
            if point_1 in l:
                index_1 = index
            if point_2 in l:
                index_2 = index
        # both are in the list
        if index_1 is not None and index_2 is not None:
            # both are in the same circuit
            if index_1 == index_2:
                continue
            # fuse 2 lists
            else:
                i_1, i_2 = min(index_1, index_2), max(index_1, index_2)
                fused_list = lists[i_1] + lists[i_2]
                lists = lists[:i_1] + lists[i_1 + 1 : i_2] + lists[i_2 + 1 :]
                lists.append(fused_list)
        # add to list
        elif index_1 is not None:
            lists[index_1].append(point_2)
        # add to list
        elif index_2 is not None:
            lists[index_2].append(point_1)
        # create new list
        else:
            lists.append([point_1, point_2])

    length_lists = sorted([len(x) for x in lists])
    return prod(length_lists[-3:])


def part_2(data):
    data = [
        (i, [int(number) for number in line.split(",")])
        for i, line in enumerate(data.split("\n"))
    ]

    distances = []
    for i in range(len(data) - 1):
        index_1, p1 = data[i]
        for j in range(i + 1, len(data)):
            index_2, p2 = data[j]
            distances.append((distance(p1, p2), index_1, index_2))
    distances = sorted(distances, key=lambda x: x[0])
    lists = []
    while sum([len(x) for x in lists]) < len(data) or len(lists) != 1:
        # see if the point are already in a list
        dis, point_1, point_2 = distances.pop(0)
        index_1 = index_2 = None
        for index, l in enumerate(lists):
            if point_1 in l:
                index_1 = index
            if point_2 in l:
                index_2 = index
        if index_1 is not None and index_2 is not None:
            if index_1 == index_2:
                continue
            else:
                i_1, i_2 = min(index_1, index_2), max(index_1, index_2)
                fused_list = lists[i_1] + lists[i_2]
                lists = lists[:i_1] + lists[i_1 + 1 : i_2] + lists[i_2 + 1 :]
                lists.append(fused_list)
        elif index_1 is not None:
            lists[index_1].append(point_2)
        elif index_2 is not None:
            lists[index_2].append(point_1)
        else:
            lists.append([point_1, point_2])

    return data[point_1][1][0] * data[point_2][1][0]


if __name__ == "__main__":
    t0 = time.time()

    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}\t\t\t{-t0 + (t1 := time.time())}s")
    print(f"Part 2: {part_2(data)}\t\t{-t1 + time.time()}s")
