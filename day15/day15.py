"""

Advent of Code 2024 - Day 15

"""

import time
import sys
from collections import defaultdict, Counter
import numpy as np
from ast import literal_eval
from itertools import product
import re
import heapq
import math
from copy import deepcopy


with open('day15.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    warehouse, movements = file.read().split("\n\n")
    warehouse = [[char for char in elem] for elem in warehouse.split("\n")]
    movements = [char for char in movements if char != "\n"]

warehouse = np.array(warehouse)
elf = deepcopy(warehouse)

# Part 1

start_time = time.perf_counter()

movement_map = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}

start = None
for r in range(warehouse.shape[0]):
    if start is not None:
        break
    for c in range(warehouse.shape[1]):
        if warehouse[r, c] == "@":
            start = (r, c)
            break

r, c = start
for move in movements:
    dr, dc = movement_map[move]
    rr, cc = r + dr, c + dc
    if warehouse[rr, cc] == "#":
        continue

    if warehouse[rr, cc] == ".":
        warehouse[rr, cc], warehouse[r, c] = "@", "."
        r, c = rr, cc
    else:  # warehouse[rr, cc] == "O"
        # check if a "." is available
        tr, tc = rr, cc
        potential = []
        while warehouse[tr, tc] not in [".", "#"]:
            tdr, tdc = movement_map[move]
            tr, tc = tr + tdr, tc + tdc
            potential.append((tr, tc))

        if warehouse[tr, tc] == ".":
            for potent in potential:
                warehouse[potent[0], potent[1]] = "O"
            warehouse[rr, cc], warehouse[r, c] = "@", "."
            r, c = rr, cc
        else:  # warehouse[tr, tc] == "#"
            # cannot move box
            continue

total_box_value = 0
for r in range(warehouse.shape[0]):
    for c in range(warehouse.shape[1]):
        if warehouse[r, c] == "O":
            total_box_value += 100 * r + c

print(f'Advent of Code Day 15 Answer Part 1: {total_box_value}')

# Part 2

# could not figure out in a reasonable amount of time

def print_grid(grid: np.array) -> None:
    for r in range(grid.shape[0]):
        print(" ".join(grid[r, :]))

grid = []
for r in range(elf.shape[0]):
    temp = []
    for c in range(elf.shape[1]):
        if elf[r, c] == "#":
            temp.append("#")
            temp.append("#")
        elif elf[r, c] == "O":
            temp.append("[")
            temp.append("]")
        elif elf[r, c] == ".":
            temp.append(".")
            temp.append(".")
        elif elf[r, c] == "@":
            temp.append("@")
            temp.append(".")
    grid.append(temp)

grid = np.array(grid)

print(f"elapsed time: {time.perf_counter() - start_time}")
