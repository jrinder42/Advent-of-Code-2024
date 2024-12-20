"""

Advent of Code 2024 - Day 20

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
with open('day20.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)
start = None
end = None
for r in range(arr.shape[0]):
    if start is not None and end is not None:
        break
    for c in range(arr.shape[1]):
        if arr[r, c] == "S":
            start = (r, c)
        elif arr[r, c] == "E":
            end = (r, c)

# Part 1

start_time = time.perf_counter()

def get_cheats(arr):
    cheats = set()
    for r in range(1, arr.shape[0] - 1):
        for c in range(arr.shape[1]):
            if arr[r - 1, c] != "#" and arr[r + 1, c] != "#":
                cheats.add(((r, c), (r - 1, c)))
                cheats.add(((r, c), (r + 1, c)))
    for c in range(1, arr.shape[1] - 1):
        for r in range(arr.shape[0]):
            if arr[r, c - 1] != "#" and arr[r, c + 1] != "#":
                cheats.add(((r, c), (r, c - 1)))
                cheats.add(((r, c), (r, c + 1)))
    return list(cheats)

def get_moves(current, arr, cheat=None):
    if cheat is not None:
        cheat, new_move = cheat
    moves = []
    r, c = current
    for pair in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        dr = r + pair[0]
        dc = c + pair[1]
        if 0 <= dr < arr.shape[0] and 0 <= dc < arr.shape[1]:# and arr[dr, dc] != "#":
            if arr[dr, dc] != "#":
                moves.append(((dr, dc), 1))
            if cheat is not None and (dr, dc) == cheat:
                moves.append((new_move, 1))

    return moves

def dijkstra(start, arr, cheat=None):
    # Dictionary to store the shortest path from start to each node
    shortest_paths = {start: 0}

    # Priority queue to explore the graph: stores (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node == end:
            return current_distance

        # Explore neighbors
        for neighbor, weight in get_moves(current_node, arr, cheat):
            distance = current_distance + weight

            # Only consider this new path if it's better
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1

cheats = get_cheats(arr)
savings = []
base = d = dijkstra(start, arr)
for i, cheat in enumerate(cheats):
    # need + 1 for the move after the wall
    d = dijkstra(start, arr, cheat) + 1
    if d < base:
        save = base - d
        savings.append(save)

c = Counter(savings)
c = dict(sorted(c.items(), key=lambda item: item[0]))
total = 0
for key, value in c.items():
    if key >= 100:
        total += value

print(f'Advent of Code Day 20 Answer Part 1: {total}')

# Part 2

# part 1 was super slow (~550 seconds, so this would take forever)

print(f"elapsed time: {time.perf_counter() - start_time}")
