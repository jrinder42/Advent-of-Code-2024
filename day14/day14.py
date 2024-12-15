"""

Advent of Code 2024 - Day 14

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


robots = []
pmax, pmin = None, None
with open('day14.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        position, velocity = line.split()
        px, py = [int(elem) for elem in re.findall(r"[-]?\d+", position)]
        vx, vy = [int(elem) for elem in re.findall(r"[-]?\d+", velocity)]
        robots.append((px, py, vx, vy))

# Part 1

start_time = time.perf_counter()

#rmax, cmax = 7, 11  # test
rmax, cmax = 103, 101

steps = 100
final_pos = []
for bot in robots:
    pos = (bot[0], bot[1])
    for _ in range(steps):
        # (position + velocity) % grid bounds
        new_r, new_c = (pos[0] + bot[2]), (pos[1] + bot[3])
        new_r = (new_r % cmax + cmax) % cmax
        new_c = (new_c % rmax + rmax) % rmax
        pos = (new_r, new_c)
    final_pos.append(pos)

if rmax % 2 == 0:
    r_quad = [(0, rmax // 2), (rmax // 2, rmax)]
else:
    r_quad = [(0, rmax // 2), (rmax // 2 + 1, rmax)]

if cmax % 2 == 0:
    c_quad = [(0, cmax // 2), (cmax // 2, cmax)]
else:
    c_quad = [(0, cmax // 2), (cmax // 2 + 1, cmax)]

zones = defaultdict(int)
for i, quad in enumerate(product(r_quad, c_quad)):
    for bot in final_pos:
        x, y = bot
        if quad[1][0] <= x < quad[1][1] and quad[0][0] <= y < quad[0][1]:
            zones[i] += 1

print(f'Advent of Code Day 14 Answer Part 1: {math.prod(zones.values())}')

# Part 2

# silly part 2

print(f"elapsed time: {time.perf_counter() - start_time}")
