"""

Advent of Code 2024 - Day 6

"""

from ast import literal_eval
from collections import deque
import numpy as np
from copy import deepcopy


arr = []
with open('day06.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)

# Part 1

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

# cycles with graphs, but too time-consuming
