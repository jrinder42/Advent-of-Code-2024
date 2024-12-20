"""

Advent of Code 2024 - Day 19

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



with open('day19.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    avail_towels, designs = file.read().split("\n\n")
    avail_towels = avail_towels.split(", ")
    designs = [design for design in designs.split("\n")]

longest = None
for elem in avail_towels:
    if longest is None or len(elem) > longest:
        longest = len(elem)

# Part 1

start_time = time.perf_counter()

# bfs
total = 0
for design in designs:
    # start_idx, end_idx
    stack = deque([(0, 1)])
    seen = set()
    special_stack = []
    while stack:
        left_pointer, right_pointer = stack.popleft()
        # a little short-circuiting to help speed things up a bit
        while right_pointer <= len(design) and right_pointer - left_pointer <= longest:
            point = design[left_pointer:right_pointer]
            new_coord = left_pointer + len(point), left_pointer + len(point) + 1
            # kinda janky logic
            if design[left_pointer:right_pointer] in avail_towels and new_coord not in seen:
                seen.add(new_coord)
                stack.append(new_coord)
                if left_pointer + len(point) + 1 > len(design):
                    special_stack.append(new_coord)

            right_pointer += 1

        left_pointer += 1

    if special_stack:
        total += 1

print(f'Advent of Code Day 19 Answer Part 1: {total}')

# Part 2

print(f"elapsed time: {time.perf_counter() - start_time}")
