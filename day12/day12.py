"""

Advent of Code 2024 - Day 12

"""

import time
from collections import defaultdict
import numpy as np
from ast import literal_eval


arr = []
with open('day12.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([char for char in line])

arr = np.array(arr)

# Part 1

start_time = time.perf_counter()

def same(r, c, arr):
    potential = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    moves = []
    for dr, dc in potential:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < arr.shape[0] and 0 <= nc < arr.shape[1] and arr[nr, nc] == arr[r, c]:
            moves.append((nr, nc))

    return moves

seen = set()
regions = []  # list of sets
while len(seen) != arr.shape[0] * arr.shape[1]:
    for r in range(arr.shape[0]):
        for c in range(arr.shape[1]):
            stack = [(r, c)]
            temp_region = []
            while stack:
                point = stack.pop()
                if point not in seen:
                    seen.add(point)
                    temp_region.append(point)
                    for move in same(point[0], point[1], arr):
                        stack.append(move)

            if temp_region:
                regions.append(temp_region)

def perimeter(points: list):
    """
    Example:
        elem is at point [1, 2]
        it will make the equality:
            N(1, 2) == S(0, 2)
            W(1, 2) == E(1, 1)
            etc.
    """
    edges = defaultdict(int)
    for point in points:
        r, c = point
        edges[f"N{(point)}"] += 1
        edges[f"S{(r - 1, c)}"] += 1

        edges[f"E{(point)}"] += 1
        edges[f"W{(r, c + 1)}"] += 1

        edges[f"W{(point)}"] += 1
        edges[f"E{(r, c - 1)}"] += 1

        edges[f"S{(point)}"] += 1
        edges[f"N{(r + 1, c)}"] += 1

    total = 0
    for key, value in edges.items():
        if value == 1:
            total += 1

    return total // 2

total_cost = 0
for region in regions:
    area = len(region)
    item = arr[region[0][0], region[0][1]]
    per = perimeter(region)
    cost = area * per
    total_cost += cost

print(f'Advent of Code Day 12 Answer Part 1: {total_cost}')

# Part 2

def create_edges(points):
    """
    Creates edges or region, from part 1
    """
    edges = defaultdict(int)
    for point in points:
        r, c = point
        edges[f"N{(point)}"] += 1
        edges[f"S{(r - 1, c)}"] += 1

        edges[f"E{(point)}"] += 1
        edges[f"W{(r, c + 1)}"] += 1

        edges[f"W{(point)}"] += 1
        edges[f"E{(r, c - 1)}"] += 1

        edges[f"S{(point)}"] += 1
        edges[f"N{(r + 1, c)}"] += 1

    return edges

def sides(points, light=None):
    edges = create_edges(points)

    # edge is unique i.e. not in the middle of a shape
    lst = []
    for key, value in edges.items():
        if value == 1:
            lst.append(key)

    # get edge set for every direction of a plot i.e. how to slice a plot
    freq_set = defaultdict(set)
    for elem in lst:
        p, tup = elem[0], literal_eval(elem[1:])
        r, c = tup
        if p == "E":
            freq_set[f"E{c}"].add((r, c))
        elif p == "W":
            freq_set[f"W{c}"].add((r, c))
        elif p == "N":
            freq_set[f"N{r}"].add((r, c))
        elif p == "S":
            freq_set[f"S{r}"].add((r, c))

    total = 0
    for key, value in freq_set.items():
        # separate regions if it is a diagonal (ex4) i.e. make sure everything is on the same line
        reg = defaultdict(set)
        idx_to_use = 0 if "N" in key or "S" in key else 1
        for elem in value:
            row, col = elem
            if not (0 <= row < arr.shape[0] and 0 <= col < arr.shape[1]):
                continue

            try:
                ite = arr[elem]
            except IndexError:
                continue

            if ite == light:
                reg[elem[idx_to_use]].add(elem)

        # now do what we did in part 1 --> measure gaps by looking at region diffs
        for kk, vv in reg.items():
            if "N" in key or "S" in key:
                fl = sorted([coord[1] for coord in vv])
            else:  # "E" in kk or "W" in kk
                fl = sorted([coord[0] for coord in vv])
            diff = np.diff(fl) if len(fl) > 1 else [1]
            total += 1
            for elem in diff:
                # this means that there is a gap between segments aka it is not contiguous
                if elem > 1:
                    total += 1

    return total

total_cost = 0
for region in regions:
    area = len(region)
    item = arr[region[0][0], region[0][1]]
    side = sides(region, light=item)
    cost = area * side
    total_cost += cost

print(f'Advent of Code Day 12 Answer Part 2: {total_cost}')

print(f"elapsed time: {time.perf_counter() - start_time}")
