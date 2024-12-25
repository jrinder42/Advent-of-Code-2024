"""

Advent of Code 2024 - Day 25

"""

import time
import sys
from collections import defaultdict, Counter, deque
import numpy as np
from ast import literal_eval
from itertools import product
import re
import heapq
import math
from copy import deepcopy


arrs = []
with open('day25.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    grids = file.read().split("\n\n")

for grid in grids:
    arrs.append([[char for char in elem] for elem in grid.split("\n")])
    arrs[-1] = np.array(arrs[-1])

locks = []
keys = []
for arr in arrs:
    if all(elem == "#" for elem in arr[0, :]):
        locks.append(arr)
    if all(elem == "#" for elem in arr[arr.shape[0] - 1, :]):
        keys.append(arr)

# Part 1

start_time = time.perf_counter()

lock_pin_heights = []
for lock in locks:
    pin_heights = []
    for col in range(lock.shape[1]):
        height = lock[:, col].tolist().count("#") - 1
        pin_heights.append(height)
    lock_pin_heights.append(pin_heights)

key_pin_heights = []
for key in keys:
    pin_heights = []
    for col in range(key.shape[1]):
        height = key[:, col].tolist().count("#") - 1
        pin_heights.append(height)
    key_pin_heights.append(pin_heights)

# index: min = 0, max = 5
total = 0
for left, right in product(lock_pin_heights, key_pin_heights):
    count = 0
    for i in range(len(left)):
        if left[i] + right[i] <= 5:
           count += 1
    total += count == len(left)

print(f'Advent of Code Day 25 Answer Part 1: {total}')

# Part 2

# cannot do as I do not have all 49 stars :(

print(f"elapsed time: {time.perf_counter() - start_time}")
