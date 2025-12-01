# Advent of Code 2025 - day 1

import re
INPUT = "input1"
# INPUT = "testinput1"

with open(INPUT) as f:
    data = f.readlines()

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

print("Part 1:", counter)
print("Part 2:", counter + counter_pass)



