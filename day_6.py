# Advent of Code 2025 - day 6

import re
import time

import numpy as np

INPUT = "input6"
# INPUT = "testinput6"


def part_1(data):
    data = data.split("\n")
    rows, operators = data[:-1], data[-1]
    operators = re.findall(r"([+*])", operators)

    numbers = []
    for row in rows:
        new_row = [int(x) for x in re.findall(r"(\d+)", row)]
        numbers.append(new_row)
    res = 0
    for index in range(len(operators)):
        if operators[index] == "+":
            number = sum([numbers[i][index] for i in range(len(numbers))])
        else:
            number = 1
            for i in range(len(numbers)):
                number *= numbers[i][index]
        res += number
    return res


def part_2_numpy(data):
    data = data.split("\n")
    rows, operators = data[:-1], re.findall(r"[+*]", data[-1])

    rows = np.array([[char for char in line] for line in rows])
    _, m = rows.shape

    res = 0
    op = operators.pop()
    curr_res = 1 if op == "*" else 0

    for col in range(m - 1, -1, -1):
        curr_col = "".join(rows[:, col]).replace(" ", "")
        if len(curr_col) == 0:
            res += curr_res
            op = operators.pop()
            curr_res = 1 if op == "*" else 0
        else:
            if op == "*":
                curr_res *= int(curr_col)
            else:
                curr_res += int(curr_col)

    return res + curr_res


def part_2(data):
    data = data.split("\n")
    rows, operators = data[:-1], data[-1]
    operators = re.findall(r"([+*])", operators)

    op = operators.pop()
    res = 0
    current_res = 0 if op == "+" else 1

    # walk through the input backwards
    for char_index in range(len(rows[0]) - 1, -1, -1):
        new_number = ""
        for row_index in range(len(rows)):
            new_number += rows[row_index][char_index]
        new_number = re.findall(r"(\d+)", new_number)
        if new_number:
            # there is a numbers, use the operator
            if op == "+":
                current_res += int(new_number[0])
            elif op == "*":
                current_res *= int(new_number[0])
        else:
            # there is no number, move on to the next operator
            res += current_res
            op = operators.pop()
            current_res = 0 if op == "+" else 1
    res += current_res
    return res


if __name__ == "__main__":
    t0 = time.time()

    with open(INPUT) as f:
        data = f.read()

    print(f"Part 1: {part_1(data)}\t\t{-t0 + (t1 := time.time())}s")
    print(f"Part 2: {part_2(data)}\t\t{-t1 + time.time()}s")
