# Advent of Code 2025 - day 9

import time

import numpy as np

INPUT = "input9"
GRID_SIZE = 100000
# INPUT = "testinput9"
# GRID_SIZE = 14


def part_1(data):
    red_tiles = [[int(x) for x in line.split(",")] for line in data.split("\n")]

    max_area = 0
    for i in range(len(red_tiles) - 1):
        for j in range(i + 1, len(red_tiles)):
            area = abs(red_tiles[i][0] - red_tiles[j][0] + 1) * abs(
                red_tiles[i][1] - red_tiles[j][1] + 1
            )
            max_area = max(area, max_area)

    return max_area


def cut_line(p1, p2, line):
    x_1, y_1 = p1
    x_2, y_2 = p2

    x_1, x_2 = sorted((x_1, x_2))
    y_1, y_2 = sorted((y_1, y_2))

    (l_x_1, l_y_1), (l_x_2, l_y_2) = line

    # vertical
    if l_x_1 == l_x_2:
        l_y_1, l_y_2 = sorted((l_y_1, l_y_2))
        if x_1 < l_x_1 < x_2:
            if not (y_1 >= l_y_2 or y_2 <= l_y_1):
                return True
    else:
        l_x_1, l_x_2 = sorted((l_x_2, l_x_1))
        if y_1 < l_y_1 < y_2:
            if not (x_1 >= l_x_2 or x_2 <= l_x_1):
                return True
    return False


def cut_lines(p1, p2, lines):
    for line in lines:
        if cut_line(p1, p2, line):
            # # print(line)
            return True
    return False


def check_outside(p1, p2, lines):
    x_1, y_1 = p1
    x_2, y_2 = p2

    x_1, x_2 = sorted((x_1, x_2))
    y_1, y_2 = sorted((y_1, y_2))


def part_2(data):
    t0 = time.time()
    red_tiles = [[int(x) for x in line.split(",")] for line in data.split("\n")]

    lines = []
    for i, tile in enumerate(red_tiles):
        lines.append([tile, red_tiles[(i + 1) % len(red_tiles)]])
    # # print(lines)

    # get squares:
    max_area = 0

    for i, tile_1 in enumerate(red_tiles[:-1]):
        for tile_2 in red_tiles[i + 1 :]:
            # # print()
            # # print(tile_1, tile_2)
            # # print("cut_lines", cut_lines(tile_1, tile_2, lines))
            if not cut_lines(tile_1, tile_2, lines):
                # check if outside
                area = abs(tile_1[0] - tile_2[0] + 1) * abs(tile_1[1] - tile_2[1] + 1)
                max_area = max(area, max_area)
    return max_area


def part_2aue(data):
    grid_shape = (
        max([x[1] for x in red_tiles]) + 1,
        max([x[0] for x in red_tiles]) + 1,
    )

    grid = np.empty(grid_shape, str)
    grid.fill(".")

    for i in range(len(red_tiles)):
        x_1, y_1 = red_tiles[i]
        x_2, y_2 = red_tiles[(i + 1) % len(red_tiles)]

        x_1, x_2 = sorted((x_1, x_2))
        y_1, y_2 = sorted((y_1, y_2))

        if x_1 == x_2:
            grid[y_1 : y_2 + 1, x_1] = "#"
        if y_1 == y_2:
            grid[y_1, x_1 : x_2 + 1] = "#"

    # # print("green", (t1 := time.time()) - t0)

    for x in range(grid_shape[1]):
        for y in range(grid_shape[0]):
            if grid[y, x] == ".":
                if (
                    sum(grid[0:y, x] == "#") % 2 == 1
                    and sum(grid[y:, x] == "#") % 2 == 1
                ):
                    grid[y, x] = "n"

    # # print("filled area", (t2 := time.time()) - t1)


def part_2(data):
    red_tiles = {
        tuple([int(x) for x in line.split(",")]): True for line in data.split("\n")
    }

    x_values = [tile[0] for tile in red_tiles]
    y_values = [tile[1] for tile in red_tiles]
    # print(min(x_values), max(x_values))
    # print(min(y_values), max(y_values))

    # print(len(set(x_values)), len(set(y_values)))
    x_set = sorted(list(set(x_values)))
    y_set = sorted(list(set(y_values)))
    mapped_x_values = {
        new_value: old_value for new_value, old_value in enumerate(x_set)
    }
    get_x_value = {old_value: new_value for new_value, old_value in enumerate(x_set)}
    mapped_y_values = {
        new_value: old_value for new_value, old_value in enumerate(y_set)
    }
    get_y_value = {old_value: new_value for new_value, old_value in enumerate(y_set)}
    # print(x_set)
    # print(mapped_x_values)
    # print(mapped_y_values)

    red_tiles = [(get_x_value[x], get_y_value[y]) for x, y in red_tiles]

    green_tiles = {}

    for i, tile_1 in enumerate(list(red_tiles)[:-1]):
        for tile_2 in list(red_tiles)[i + 1 :]:
            x_1, y_1 = tile_1
            x_2, y_2 = tile_2
            if x_1 == x_2:
                for y in range(min(y_1, y_2) + 1, max(y_1, y_2)):
                    green_tiles[(x_1, y)] = True
            if y_1 == y_2:
                for x in range(min(x_1, x_2) + 1, max(x_1, x_2)):
                    green_tiles[(x, y_1)] = True

    grid = np.empty(
        (len(x_set), len(y_set)),
        str,
    )
    grid.fill(".")

    for red in red_tiles:
        grid[red[1], red[0]] = "O"
    # print("filled red tiles", time.time())

    for green in green_tiles:
        grid[green[1], green[0]] = "#"
    # # print("filled green tiles", time.time())

    # for x in range(grid.shape[1]):
    #     for y in range(grid.shape[0]):
    #         if grid[x, y] != ".":
    #             continue

    #         if (
    #             sum((grid[0:x, y] == "#")) % 2 == 1
    #             and sum((grid[x:, y] == "#")) % 2 == 1
    #         ):
    #             grid[x, y] = "n"

    # fill the inner parts

    start_point = (list(grid[0, :]).index("#"), 1)

    q = [start_point]
    seen_tiles = {}

    while q:
        curr_x, curr_y = q.pop()
        seen_tiles[(curr_x, curr_y)] = True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                grid[curr_x + dx, curr_y + dy] == "."
                and (curr_x + dx, curr_y + dy) not in seen_tiles
            ):
                q.append((curr_x + dx, curr_y + dy))

    for seen in seen_tiles:
        grid[seen[0], seen[1]] = "n"

    # # print("filled area", time.time())

    # string = "\n".join(["".join(char for char in line) for line in grid])

    # with open("grid_day_9.txt", "w") as f:
    #     f.write(string)
    # return 3
    # for red in red_tiles:
    #     grid[red[1], red[0]] = "O"
    # # # print(grid)
    # # print("filled red tiles again", time.time())

    max_area = 0
    for i, tile_1 in enumerate(list(red_tiles)[:-1]):
        for tile_2 in list(red_tiles)[i + 1 :]:
            x_1, y_1 = tile_1
            x_2, y_2 = tile_2

            x_1, x_2 = sorted((x_1, x_2))
            y_1, y_2 = sorted((y_1, y_2))
            grid_part = grid[y_1 : y_2 + 1, x_1 : x_2 + 1]
            # # # print(tile_1, tile_2, grid_part)
            # # # print(np.sum(grid_part == "."))
            # print(grid)
            if np.sum(grid_part == ".") == 0:
                area = (x_2 - x_1 + 1) * (y_2 - y_1 + 1)
                # print()
                # print(x_2, mapped_x_values[x_2])
                # print(x_1, mapped_x_values[x_1])
                # print(y_1, mapped_y_values[y_1])
                # print(y_2, mapped_y_values[y_2])

                area = (mapped_x_values[x_2] - mapped_x_values[x_1] + 1) * (
                    mapped_y_values[y_2] - mapped_y_values[y_1] + 1
                )
                # print(area)
                max_area = max(area, max_area)

    return max_area


if __name__ == "__main__":
    t0 = time.time()

    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}\t\t{-t0 + (t1 := time.time())}s")
    print(f"Part 2: {part_2(data)}\t\t{-t1 + time.time()}s")
