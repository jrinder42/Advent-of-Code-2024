"""

Advent of Code 2024 - Day 22

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

nums = []
with open('day22.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        nums.append(literal_eval(line))

# Part 1

start_time = time.perf_counter()

def mix(num, secret_num):
    return num ^ secret_num

def prune(secret_num):
    return secret_num % 16777216

def evolve(secret_num):
    num = secret_num
    num *= 64
    # mix this into the secret_num - bitwise xor
    secret_num = mix(num, secret_num)
    # prune the secret number
    secret_num = prune(secret_num)

    num = secret_num // 32
    secret_num = mix(num, secret_num)
    secret_num = prune(secret_num)

    num = secret_num * 2048
    secret_num = mix(num, secret_num)
    secret_num = prune(secret_num)

    return secret_num

def generate_secret_num(init_num, steps):
    for _ in range(steps):
        init_num = evolve(init_num)

    return init_num

total = 0
for num in nums:
    total += generate_secret_num(num, 2000)

print(f'Advent of Code Day 22 Answer Part 1: {total}')

# Part 2

# no idea how to do part 2

def generate_secret_num_p2(init_num, steps):
    vals = [int(str(init_num)[-1])]
    for _ in range(steps):
        init_num = evolve(init_num)
        vals.append(int(str(init_num)[-1]))
        diff = vals[-1] - vals[-2]

    return vals

print(f"elapsed time: {time.perf_counter() - start_time}")
