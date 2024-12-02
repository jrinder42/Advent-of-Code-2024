"""

Advent of Code 2024 - Day 2

"""

from ast import literal_eval


arr = []
with open('day02.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        arr.append([literal_eval(elem) for elem in line.split()])

# Part 1

def check_line(base):
    diffs = [base[1:][elem] - base[:-1][elem] for elem in range(len(base) - 1)]
    cond1 = all(elem < 0 for elem in diffs) or all(elem > 0 for elem in diffs)
    cond2 = all(1 <= abs(elem) <= 3 for elem in diffs)

    return cond1 and cond2

total = 0
for base in arr:
    total += check_line(base)

print(f'Advent of Code Day 2 Answer Part 1: {total}')

# Part 2

# brute-force mess
total = 0
for base in arr:
    diffs = [base[1:][elem] - base[:-1][elem] for elem in range(len(base) - 1)]

    check = check_line(base)
    if not check:
        for i in range(len(base)):
            temp_arr = base[:i] + base[i + 1:]
            if check_line(temp_arr):
                total += 1
                break
    else:
        total += 1

print(f'Advent of Code Day 2 Answer Part 2: {total}')
