# Advent of Code 2025 - day 1


INPUT = "input1"
# INPUT = "testinput1"


def part_1(data):
    counter = 0
    pos = 50
    for d in data:
        direction, distance = d[0], int(d[1:])
        if direction == "L":
            pos = (pos - distance) % 100
        else:
            pos = (pos + distance) % 100
        if pos == 0:
            counter += 1
    return counter


def part_2(data):
    counter = 0
    counter_pass = 0
    pos = 50
    for d in data:
        direction, distance = d[0], int(d[1:])
        if direction == "L":
            if pos == 0:
                counter_pass -= 1
            pos -= distance
            while pos < 0:
                counter_pass += 1
                pos += 100
        else:
            pos += distance
            while pos > 99:
                counter_pass += 1
                pos -= 100
            if pos == 0:
                counter_pass -= 1

        if pos == 0:
            counter += 1
    return counter + counter_pass


if __name__ == "__main__":
    with open(INPUT) as f:
        data = f.readlines()

    print("Part 1:", part_1(data))
    print("Part 2:", part_2(data))
