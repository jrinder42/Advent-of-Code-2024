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


network = defaultdict(set)
with open('day23.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        key, value = line.split("-")
        network[key].add(value)
        network[value].add(key)

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
            if (connected_computer == key and elem[1] == size) or elem[2].count(connected_computer) == 0:
                new_list = elem[2] + [connected_computer]
                stack.append([connected_computer, increment + 1, new_list])

total_sets = [set(elem[2]) for elem in total]
seen = []
for elem in total_sets:
    if elem not in seen:
        seen.append(elem)

print(f'Advent of Code Day 23 Answer Part 1: {len(seen)}')

# Part 2

# key to part 2 is changing the data structure from a list to a set
# goes from O(n) lookup --> O(1) lookup

def connected(network, computer, computer_list):
    for elem in computer_list:
        if elem not in network[computer] and computer not in network[elem]:
            return False
    return True

# bfs
msize = [0, []]
total = []
for key, value in network.items():
    stack = deque([[key, 1, {key}]])
    while stack:
        elem = stack.popleft()
        # weird issue where elem[1] is not incrementing, but will ignore as it is necessarily needed
        #if elem[1] > msize[0]:
        if len(elem[2]) > msize[0]:
            #msize = [elem[1], elem[2]]
            msize = [len(elem[2]), elem[2]]

        connected_computers = network[elem[0]]
        increment = elem[1]
        for connected_computer in connected_computers:
            if connected_computer not in elem[2] and connected(network, connected_computer, elem[2]):
                new_set = elem[2]
                new_set.add(connected_computer)
                stack.append([connected_computer, increment + 1, new_set])


password = ",".join(sorted(msize[1]))

print(f'Advent of Code Day 23 Answer Part 2: {password}')

print(f"elapsed time: {time.perf_counter() - start_time}")
