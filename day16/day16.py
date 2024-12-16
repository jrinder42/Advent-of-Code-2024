"""

Advent of Code 2024 - Day 16

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


arr = []
with open('day16.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([elem for elem in line])

arr = np.array(arr)

# Part 1

start_time = time.perf_counter()

def get_moves(current, arr, dir):
    r, c = current
    dr, dc = dir  # (1, 0) means going down
    opposite = (-dr, -dc)
    moves = []
    for nr, nc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if (nr, nc) == opposite:
            continue

        pr, pc = r + nr, c + nc
        if arr[(pr, pc)] != "#":  # can be "." or "E"
            # 1001 because we turn (1000) + move (1)
            val = 1 if (nr, nc) == dir else 1001

            moves.append(
                [
                    (pr, pc),
                    val,
                    (nr, nc)
                ]
            )

    return moves

def dijkstra(start, arr):
    # Dictionary to store the shortest path from start to each node
    shortest_paths = {start: 0}

    # Priority queue to explore the graph: stores (distance, node)
    # start facing east
    priority_queue = [(0, start, (0, 1))]

    while priority_queue:
        current_distance, current_node, current_dir = heapq.heappop(priority_queue)
        if arr[current_node] == "E":
            return current_distance

        # Explore neighbors
        for neighbor, weight, dir in get_moves(current_node, arr, current_dir):
            distance = current_distance + weight

            # Only consider this new path if it's better
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, dir))

    return -1

start = None
for r in range(arr.shape[0]):
    if start is not None:
        break
    for c in range(arr.shape[1]):
        if arr[r, c] ==  "S":
            start = (r, c)
            break

d = dijkstra(start, arr)

print(f'Advent of Code Day 16 Answer Part 1: {d}')

# Part 2

# did now want to spend the time doing it

print(f"elapsed time: {time.perf_counter() - start_time}")
