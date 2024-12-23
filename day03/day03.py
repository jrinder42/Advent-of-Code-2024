"""

Advent of Code 2024 - Day 3

"""

import math
from ast import literal_eval
import re


text = []
with open('day03.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        text.append(line)

text = ["".join(text)]

pattern = r'mul\((\d+),\s*(\d+)\)'

total = 0
for elem in text:
    matches = re.findall(pattern, elem)

    for row in matches:
        left, right = literal_eval(row[0]), literal_eval(row[1])
        total += left * right

print(f'Advent of Code Day 3 Answer Part 1: {total}')

# Part 2

pattern = r'mul\(\d+\s*,\s*\d+\)|do\(\)|don\'t\(\)'
matches = re.findall(pattern, text[0])
total = 0
skip = False
for match in matches:
    if not skip and match.startswith('mul'):
        nums = re.findall('\d+', match)
        total += math.prod([int(num) for num in nums])
    elif match == "do()":
        skip = False
    else:  # match == "don\'t()"
        skip = True

print(f'Advent of Code Day 3 Answer Part 2: {total}')
