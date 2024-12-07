"""

Advent of Code 2024 - Day 7

"""

from ast import literal_eval


total_dict = {}
with open('day07.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        left, right = line.split(': ')
        left = literal_eval(left)
        right = [literal_eval(elem) for elem in right.split()]
        total_dict[left] = right


# Part 1

# bfs
total = 0
for totals, nums in total_dict.items():
    stack = [(0, nums[0])]
    while stack:
        idx, num = stack.pop()
        n = len(nums)
        if idx < n - 1:
            idx += 1
            next_num = nums[idx]
            for elem in ["+", "*"]:
                if elem == "+":
                    stack.append((idx, next_num + num))
                else:  # elem == "*"
                    stack.append((idx, next_num * num))
        elif num == totals:
            total += num
            break

print(f'Advent of Code Day 7 Answer Part 1: {total}')

# Part 2

total = 0
for totals, nums in total_dict.items():
    stack = [(0, nums[0])]
    while stack:
        idx, num = stack.pop()
        n = len(nums)
        if idx < n - 1:
            idx += 1
            next_num = nums[idx]
            for elem in ["+", "*", '||']:
                if elem == "+":
                    stack.append((idx, next_num + num))
                elif elem == "*":
                    stack.append((idx, next_num * num))
                else:  # elem == "||"
                    stack.append((idx, eval(f"{num}{next_num}")))
        elif num == totals:
            total += num
            break

print(f'Advent of Code Day 7 Answer Part 2: {total}')
