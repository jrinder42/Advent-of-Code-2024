"""

Advent of Code 2024 - Day 4

"""

import numpy as np


arr = []
with open('day04.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)

# Part 1

total = 0
for r in range(arr.shape[0]):
    row = arr[r, :].tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")

    i = r
    row = arr.diagonal(i).tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")

    if i == 0:
        continue

    row = arr.diagonal(-i).tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")

for c in range(arr.shape[1]):
    row = arr[:, c].tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")


flipped_arr = np.fliplr(arr)

for i in range(flipped_arr.shape[0]):
    row = flipped_arr.diagonal(i).tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")

    if i == 0:
        continue

    row = flipped_arr.diagonal(-i).tolist()
    str_row = "".join(row)
    total += str_row.count("XMAS")
    str_row = "".join(row[::-1])
    total += str_row.count("XMAS")


print(f'Advent of Code Day 4 Answer Part 1: {total}')

# Part 2

base = [
    [["M", ".", "M"], [".", "A", ""], ["S", ".", "S"]],
    [["S", ".", "S"], [".", "A", ""], ["M", ".", "M"]],
    [["M", ".", "S"], [".", "A", ""], ["M", ".", "S"]],
    [["S", ".", "M"], [".", "A", ""], ["S", ".", "M"]]
]
for i in range(len(base)):
    base[i] = np.array(base[i])

base_diags = []
for elem in base:
    fl = np.fliplr(elem)
    base_diags.append((elem.diagonal(0), fl.diagonal(0)))

total = 0
for r in range(arr.shape[0]):  # can also have -2
    for c in range(arr.shape[1]):  # can also have -2
        r_range = r + 3
        c_range = c + 3

        sub = arr[r:r_range, c:c_range]
        main_diag = sub.diagonal(0)
        off_diag = np.fliplr(sub).diagonal(0)

        count = 0
        for left, right in base_diags:
            if np.array_equal(main_diag, left) and np.array_equal(main_diag, right):
                count += 1
            if np.array_equal(off_diag, left) and np.array_equal(off_diag, right):
                count += 1

        if count == 2:
            total += 1

print(f'Advent of Code Day 4 Answer Part 2: {total}')
