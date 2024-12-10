"""

Advent of Code 2024 - Day 10

"""

import time
from ast import literal_eval
import numpy as np
from collections import defaultdict


arr = []
with open('day10.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([literal_eval(num) for num in line])

arr = np.array(arr)

# Part 1

start_time = time.perf_counter()

starting_pos = []
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        if arr[r, c] == 0:
            starting_pos.append([r, c])

def valid_moves(current_pos, arr):
    r, c = current_pos
    for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if 0 <= r + dr < arr.shape[0] and 0 <= c + dc < arr.shape[1]:
            move = arr[r + dr, c + dc]
            step_size = move - arr[r, c]
            # gradual uphill of step size 1
            if step_size == 1:
                yield r + dr, c + dc

# bfs
peaks = defaultdict(set)
for trail in starting_pos:
    stack = [trail]
    while stack:
        pos = stack.pop()
        for move in valid_moves(pos, arr):
            # hit peak
            if arr[move] == 9:
                peaks[tuple(trail)].add(move)
            else:
                stack.append(move)

total = 0
for trail, peak_set in peaks.items():
    total += len(peak_set)

print(f'Advent of Code Day 10 Answer Part 1: {total}')
print(f"elapsed time for part 1: {time.perf_counter() - start_time}")

# Part 2

# literally the only difference from the above is changing peaks from defaultdict(set) --> defaultdict(list)

peaks = defaultdict(list)
for trail in starting_pos:
    stack = [trail]
    while stack:
        pos = stack.pop()
        for move in valid_moves(pos, arr):
            # hit peak
            if arr[move] == 9:
                peaks[tuple(trail)].append(move)
            else:
                stack.append(move)

total = 0
for trail, peak_set in peaks.items():
    total += len(peak_set)

print(f'Advent of Code Day 10 Answer Part 2: {total}')
