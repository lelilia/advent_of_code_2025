# Advent of Code - Day 2

import time

INPUT = "input2"
# INPUT = "testinput2"


def check_range(left, right, part):

    seen = set()
    left_str, right_str = str(left), str(right)
    start_chuck = int(left_str[:len(left_str) // 2]) if len(left_str) > 1 else 1
    end_chunk = int(right_str[:(len(right_str) + 1)//2])

    for chunk in range(start_chuck, end_chunk +1):
        id = int(str(chunk) + str(chunk))
        if left <= id <= right:
            seen.add(id)

        if part == 2:
            for bit in range(1, len(str(chunk))+1):
                for length in range(len(left_str)//bit, len(right_str)//bit + 1):
                    id = int(str(chunk)[:bit] * length)
                    if left <= id <= right:
                        seen.add(id)

    return sum(list(seen))


def solve(data, part=1):
    sum = 0
    for d in data.split(","):
        left, right = [int(x) for x in d.split("-")]
        sum += check_range(left, right, part)
    return sum


if __name__ == "__main__":
    t0 = time.time()

    with open(INPUT) as f:
        data = f.read()

    sum_1 = solve(data)
    print(f"Part 1: {sum_1},     {time.time() - t0} s")

    sum_2 = solve(data, 2)
    print(f"Part 2: {sum_2},     {time.time() - t0} s")
