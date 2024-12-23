"""

Advent of Code 2024 - Day 23

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


network = defaultdict(list)
with open('day23.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        key, value = line.split("-")
        network[key].append(value)
        network[value].append(key)

# Part 1

start_time = time.perf_counter()

# bfs
size = 3
total = []
for key, value in network.items():
    stack = deque([[key, 1, [key]]])
    while stack:
        elem = stack.popleft()
        if elem[1] == size + 1:
            if elem[2][0] == elem[2][size]:
                count = 0
                for e in elem[2]:
                    if e.startswith("t"):
                        count += 1
                if count:
                    total.append(elem)
            continue

        connected_computers = network[elem[0]]
        increment = elem[1]
        for connected_computer in connected_computers:
            if (connected_computer == key and len(elem[2]) == size) or connected_computer not in elem[2]:
                new_list = elem[2] + [connected_computer]
                stack.append([connected_computer, increment + 1, new_list])

total_sets = [set(elem[2]) for elem in total]
seen = []
for elem in total_sets:
    if elem not in seen:
        seen.append(elem)

print(f'Advent of Code Day 23 Answer Part 1: {len(seen)}')

# Part 2

# will work on this a bit

print(f"elapsed time: {time.perf_counter() - start_time}")
