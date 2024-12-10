"""

Advent of Code 2024 - Day 9

"""

import time
from ast import literal_eval


nums = ""
with open('day09.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        nums = line

# Part 1

start_time = time.perf_counter()

files, free_space = [], []
for i in range(0, len(nums) - 1, 2):
    left, right = literal_eval(nums[i]), literal_eval(nums[i + 1])
    files.append(left)
    free_space.append(right)

def create_disk_map(files, free_space):
    idx = 0
    disk_map = []
    for file, space in zip(files, free_space):
        disk_map += [str(idx)] * file
        disk_map += ["."] * space
        idx += 1

    # not even -- this should be assumed
    if len(nums) % 2 == 1:
        file_map = [str(idx)] * literal_eval(nums[-1])
        disk_map += file_map

    return disk_map, idx

#disk_map = disk_map + ["."] * (n - len(disk_map))
disk_map, _ = create_disk_map(files, free_space)
n = len(disk_map)
idx = disk_map.index(".")
while not all(elem.isnumeric() for elem in disk_map): # all(elem == "." for elem in disk_map[idx:]):
    if disk_map[idx] == ".":
        num = disk_map.pop()
        while num == ".":
            num = disk_map.pop()
        disk_map[idx] = num
    idx += 1

total = 0
for i, num in enumerate(disk_map):
    total += i * literal_eval(num)

print(f'Advent of Code Day 9 Answer Part 1: {total}')
print(f"elapsed time for part 1: {time.perf_counter() - start_time}")

# Part 2

# Easy, just tedious and don't have the time
