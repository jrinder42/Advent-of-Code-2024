"""

Advent of Code 2024 - Day 18

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

memory_space = []
with open('day18.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        memory_space.append([int(elem) for elem in re.findall(r'\d+', line)])

# Part 1

start_time = time.perf_counter()

#low_bound, high_bound = 0, 7  # for the test input
low_bound, high_bound = 0, 71

arr = np.full((high_bound, high_bound), ".")

#for elem in memory_space[:12]:  # for the test input
for elem in memory_space[:1024]:
    arr[elem[0], elem[1]] = "#"

def get_moves(current, arr):
    moves = []
    r, c = current
    for pair in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        dr = r + pair[0]
        dc = c + pair[1]
        if 0 <= dr < arr.shape[0] and 0 <= dc < arr.shape[1] and arr[dr, dc] != "#":
            moves.append(((dr, dc), 1))

    return moves

def dijkstra(start, arr):
    # Dictionary to store the shortest path from start to each node
    shortest_paths = {start: 0}

    # Priority queue to explore the graph: stores (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        #if current_node == (6, 6):  # for the test input
        if current_node == (70, 70):
            return current_distance

        # Explore neighbors
        for neighbor, weight in get_moves(current_node, arr):
            distance = current_distance + weight

            # Only consider this new path if it's better
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1

d = dijkstra((0, 0), arr)  # for the test input

print(f'Advent of Code Day 18 Answer Part 1: {d}')

# Part 2

result = None
for elem in memory_space[1024:]:
    arr[elem[0], elem[1]] = "#"

    d = dijkstra((0, 0), arr)
    if d == -1:
        result = elem
        break

print(f'Advent of Code Day 18 Answer Part 2: {result}')

print(f"elapsed time: {time.perf_counter() - start_time}")
