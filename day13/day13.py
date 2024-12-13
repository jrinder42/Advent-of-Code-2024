"""

Advent of Code 2024 - Day 13

"""

import time
from collections import defaultdict
import numpy as np
from ast import literal_eval
import re
import heapq


machines = []
with open('day13.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    lines = file.read().split("\n\n")
    for row in lines:
        machine = []
        prizes = {}
        for line in row.split("\n"):
            if "Prize" in line:
                x, y = re.findall(r"\d+", line)
                prizes = {"X": int(x), "Y": int(y)}
            else:
                left, right = line.split(": ")
                button = left.split()[1]
                x, y = right.split(", ")
                x = re.findall(r"\d+", x)[0]
                y = re.findall(r"\d+", y)[0]
                machine.append({"Button": button, "X": int(x), "Y": int(y)})

        machine.append({"Prize": prizes})
        machines.append(machine)

# Part 1

start_time = time.perf_counter()

def get_moves(current, machine):
    r, c = current
    moves = []
    a, b, prize = machine
    if r + a["Y"] <= prize["Prize"]["Y"] and c + a["X"] <= prize["Prize"]["X"]:
        moves.append(((r + a["Y"], c + a["X"]), 3))
    if r + b["Y"] <= prize["Prize"]["Y"] and c + b["X"] <= prize["Prize"]["X"]:
        moves.append(((r + b["Y"], c + b["X"]), 1))
    return moves

def dijkstra(machine, start):
    # Dictionary to store the shortest path from start to each node
    shortest_paths = {(0, 0): 0}

    # Priority queue to explore the graph: stores (distance, node)
    priority_queue = [(0, start)]  # Start with the source node

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_node[0] == machine[2]["Prize"]["Y"] and current_node[1] == machine[2]["Prize"]["X"]:
            return current_distance

        # Explore neighbors
        for neighbor, weight in get_moves(current_node, machine):
            distance = current_distance + weight

            # Only consider this new path if it's better
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return -1

total = 0
for i, machine in enumerate(machines):
    result = dijkstra(machine, (0, 0))
    total += result if result != -1 else 0

print(f'Advent of Code Day 13 Answer Part 1: {total}')

# Part 2

# don't know how to do this efficiently

print(f"elapsed time: {time.perf_counter() - start_time}")
