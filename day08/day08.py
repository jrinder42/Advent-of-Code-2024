"""

Advent of Code 2024 - Day 8

"""

from ast import literal_eval
import numpy as np
from collections import defaultdict
from itertools import combinations


arr = []
with open('day08.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)

# Part 1

antennas = defaultdict(set)
for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        if arr[r, c] != ".":
            antennas[arr[r, c]].add((r, c))

potentials = set()
for key, value in antennas.items():
    for left, right in combinations(value, 2):
        dr, dc = right[0] - left[0], right[1] - left[1]
        potents = [(left[0] + dr, left[1] + dc),
                  (left[0] - dr, left[1] - dc),
                  (right[0] + dr, right[1] + dc),
                  (right[0] - dr, right[1] - dc)]
        for potent in potents:
            if potent not in value and 0 <= potent[0] < arr.shape[0] and 0 <= potent[1] < arr.shape[1]:
                potentials.add(potent)

print(f'Advent of Code Day 8 Answer Part 1: {len(potentials)}')

# Part 2

potentials = set()
for key, value in antennas.items():
    for left, right in combinations(value, 2):
        dr, dc = right[0] - left[0], right[1] - left[1]
        potents = set()

        factor = 1
        while 0 <= left[0] + factor * dr < arr.shape[0] and 0 <= left[1] + factor * dc < arr.shape[1]:
            potents.add((left[0] + factor * dr, left[1] + factor * dc))
            factor += 1

        factor = 1
        while 0 <= right[0] + factor * dr < arr.shape[0] and 0 <= right[1] + factor * dc < arr.shape[1]:
            potents.add((right[0] + factor * dr, right[1] + factor * dc))
            factor += 1

        factor = 1
        while 0 <= left[0] - factor * dr < arr.shape[0] and 0 <= left[1] - factor * dc < arr.shape[1]:
            potents.add((left[0] - factor * dr, left[1] - factor * dc))
            factor += 1

        factor = 1
        while 0 <= right[0] - factor * dr < arr.shape[0] and 0 <= right[1] - factor * dc < arr.shape[1]:
            potents.add((right[0] - factor * dr, right[1] - factor * dc))
            factor += 1

        for potent in potents:
            potentials.add(potent)

print(f'Advent of Code Day 8 Answer Part 2: {len(potentials)}')
