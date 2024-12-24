"""

Advent of Code 2024 - Day 6

"""

from ast import literal_eval
from collections import deque
import numpy as np
from copy import deepcopy
import time


arr = []
with open('day06.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)

# Part 1

start_time = time.perf_counter()

# find guard
guard = None
for r in range(arr.shape[0]):
    if guard is not None:
        break

    for c in range(arr.shape[1]):
        if arr[r, c] in ['^', 'v', '<', '>']:
            guard = [r, c, arr[r, c]]
            arr[r, c] = '.'
            break

# awful code, but gets the job done
def guard_move(arr):
    # move guard
    pos = guard
    unique_pos = set()
    unique_pos.add((pos[0], pos[1]))
    # guard is in the grid col v row
    while 0 <= pos[0] < arr.shape[1] and 0 <= pos[1] < arr.shape[0]:
        r, c = pos[0], pos[1]
        if pos[2] == '^':
            if r - 1 < 0:
                break
            # can move
            if arr[r - 1, c] == '.':
                pos = [r - 1, c, '^']
                unique_pos.add((r - 1, c))
            else:  # rotate
                pos = [r, c, '>']
        elif pos[2] == '>':
            if c + 1 >= arr.shape[1]:
                break
            # can move
            if arr[r, c + 1] == '.':
                pos = [r, c + 1, '>']
                unique_pos.add((r, c + 1))
            else:  # rotate
                pos = [r, c, 'v']
        elif pos[2] == 'v':
            if r + 1 >= arr.shape[0]:
                break
            # can move
            if arr[r + 1, c] == '.':
                pos = [r + 1, c, 'v']
                unique_pos.add((r + 1, c))
            else:  # rotate
                pos = [r, c, '<']
        elif pos[2] == '<':
            if c - 1 < 0:
                break
            # can move
            if arr[r, c - 1] == '.':
                pos = [r, c - 1, '<']
                unique_pos.add((r, c - 1))
            else:  # rotate
                pos = [r, c, '^']


    return unique_pos

unique_pos = guard_move(arr)
print(f'Advent of Code Day 6 Answer Part 1: {len(unique_pos)}')

# Part 2

potential = []
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        if arr[r, c] == ".":
            potential.append((r, c))

# awful code, but gets the job done
def guard_move_p2(arr, potent):
    # move guard
    pos = guard

    grid = deepcopy(arr)
    grid[potent] = "#"

    seen = set()
    while 0 <= pos[0] < grid.shape[1] and 0 <= pos[1] < grid.shape[0]:
        r, c = pos[0], pos[1]

        # need to convert to tuple and too lazy to change things from list --> tuple
        if tuple(pos) in seen:
            return True

        seen.add(tuple(pos))

        # main logic
        if pos[2] == '^':
            if r - 1 < 0:
                break
            # can move
            if grid[r - 1, c] == '.':
                pos = [r - 1, c, '^']
            else:  # rotate
                pos = [r, c, '>']
        elif pos[2] == '>':
            if c + 1 >= grid.shape[1]:
                break
            # can move
            if grid[r, c + 1] == '.':
                pos = [r, c + 1, '>']
            else:  # rotate
                pos = [r, c, 'v']
        elif pos[2] == 'v':
            if r + 1 >= grid.shape[0]:
                break
            # can move
            if grid[r + 1, c] == '.':
                pos = [r + 1, c, 'v']
            else:  # rotate
                pos = [r, c, '<']
        elif pos[2] == '<':
            if c - 1 < 0:
                break
            # can move
            if grid[r, c - 1] == '.':
                pos = [r, c - 1, '<']
            else:  # rotate
                pos = [r, c, '^']


    return False

total = 0
for potent in potential:
    total += guard_move_p2(arr, potent)

print(f'Advent of Code Day 6 Answer Part 2: {total}')  # ~50 seconds

print(f"elapsed time: {time.perf_counter() - start_time}")
