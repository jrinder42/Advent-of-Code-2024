"""

Advent of Code 2024 - Day 24

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


z = []
with open('day24.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    wire, logic = file.read().split("\n\n")
    wire = dict([elem.split(": ") for elem in wire.split("\n")])
    for elem in logic.split("\n"):
        left, right = elem.split(" -> ")
        l, m, r = left.split()
        z.append({"left": l, "right": r, "operation": m, "store": right})

# Part 1

start_time = time.perf_counter()

gates = {"AND": "&",
         "OR": "|",
         "XOR": "^"}

def create_value_dict(z, wire):
    value_dict = wire
    queue = deque(z)
    while queue:
        elem = queue.popleft()
        left, right = elem["left"], elem["right"]
        if left in value_dict and right in value_dict:
            lvalue = wire[left]
            rvalue = wire[right]
            op = gates[elem["operation"]]
            compute = f"{lvalue} {op} {rvalue}"
            value_dict[elem["store"]] = str(eval(compute))
        else:
            queue.append(elem)

    return value_dict

value_dict = create_value_dict(z, wire)

z_map = {}
for elem in z:
    store = elem["store"]
    if store.startswith("z"):
        z_map[int(store[1:])] = value_dict[store]

z_map = dict(sorted(z_map.items(), key=lambda item: item[0]))
snum = list(z_map.values())
snum = int("".join(snum[::-1]), 2)

print(f'Advent of Code Day 24 Answer Part 1: {snum}')

# Part 2

print(f"elapsed time: {time.perf_counter() - start_time}")
