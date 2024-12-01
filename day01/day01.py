"""

Advent of Code 2024 - Day 1

"""

from ast import literal_eval
from collections import Counter


left, right = [], []
with open('day01.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        l, r = line.split()
        l, r = literal_eval(l), literal_eval(r)
        left.append(l)
        right.append(r)

left.sort()
right.sort()
joint = zip(left, right)

# Part 1

total = sum(abs(row[0] - row[1]) for row in joint)

print(f'Advent of Code Day 1 Answer Part 1: {total}')

# Part 2

right_counter = Counter(right)
total = sum(row * right_counter.get(row, 0) for row in left)

print(f'Advent of Code Day 1 Answer Part 2: {total}')
