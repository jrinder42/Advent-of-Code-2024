"""

Advent of Code 2024 - Day 5

"""

from ast import literal_eval
from collections import deque


top = []
bottom = []
switch = False
with open('day05ex.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if not line.strip():
            switch = True
            continue

        if switch:
            eval_list = [literal_eval(num) for num in line.split(",")]
            if eval_list:
                bottom.append(eval_list)
        else:
            left, right = line.split("|")
            top.append((literal_eval(left), literal_eval(right)))

# Part 1

total = 0
for lst in bottom:
    lst_dict = {}
    for i, num in enumerate(lst):
        lst_dict[num] = i

    bad_counter = 0
    for left, right in top:
        if left in lst_dict and right in lst_dict and not lst_dict[left] < lst_dict[right]:
            bad_counter += 1

    if not bad_counter:
        n = len(lst)
        total += lst[n // 2]

print(f'Advent of Code Day 5 Answer Part 1: {total}')

# Part 2

# too time-consuming, so didn't do it
