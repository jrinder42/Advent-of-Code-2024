"""

Advent of Code 2024 - Day 11

"""

import time
from ast import literal_eval
from collections import defaultdict


stones = []
with open('day11.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        stones = [literal_eval(num) for num in line.split()]

# Part 1

start_time = time.perf_counter()

def new_stone(stone: int):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        n = len(stone)
        left, right = stone[:n // 2], stone[n // 2:]
        # literal_eval errors out
        return int(left), int(right)
    else:
        return [stone * 2024]

num_blinks = 25
for _ in range(num_blinks):
    new_stones = []
    for stone in stones:
        new_stones += new_stone(stone)
    stones = new_stones

print(f'Advent of Code Day 11 Answer Part 1: {len(stones)}')

# Part 2

stones = []
with open('day11.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        stones = [literal_eval(num) for num in line.split()]

stone_counter = defaultdict(int)
for stone in stones:
    stone_counter[stone] += 1

num_blinks = 75
for _ in range(num_blinks):
    temp_counter = defaultdict(int)
    for stone, count in stone_counter.items():
        vals = new_stone(stone)
        for val in vals:
            temp_counter[val] += count * 1
    stone_counter = temp_counter

print(f'Advent of Code Day 11 Answer Part 2: {sum(stone_counter.values())}')

print(f"elapsed time: {time.perf_counter() - start_time}")
