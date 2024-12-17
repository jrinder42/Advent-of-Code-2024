"""

Advent of Code 2024 - Day 17

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


with open('day17.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    registers, instructions = file.read().split("\n\n")
    registers = [int(elem) for elem in re.findall("\d+", registers)]
    registers = dict(zip(["A", "B", "C"], registers))
    instructions = [int(elem) for elem in re.findall("\d+", instructions)]

# opcodes, operands
instruct = zip(instructions[::2], instructions[1::2])

# Part 1

start_time = time.perf_counter()

def combo_operand(num, registers):
    if 0 <= num <= 3:
        return num
    elif num == 4:
        return registers["A"]
    elif num == 5:
        return registers["B"]
    elif num == 6:
        return registers["C"]
    return None

def opcode_instruct(instruction, registers, to_print: list):
    jump = False
    opcode, operand = instruction
    if opcode == 0:
        registers["A"] = registers["A"] // 2**combo_operand(operand, registers)
    elif opcode == 1:
        registers["B"] = registers["B"] ^ operand
    elif opcode == 2:
        registers["B"] = combo_operand(operand, registers) % 8
    elif opcode == 3:
        # do nothing
        if registers["A"] == 0:
            pass
        else:
            jump = True
    elif opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    elif opcode == 5:  # might be multiple values, comma separated
        val = combo_operand(operand, registers) % 8
        to_print.append(val)
    elif opcode == 6:
        registers["B"] = registers["A"] // 2 ** combo_operand(operand, registers)
    elif opcode == 7:
        registers["C"] = registers["A"] // 2 ** combo_operand(operand, registers)

    return registers, to_print, jump

to_print = []
idx = 0
while idx < len(instructions):
    pair = instructions[idx:idx + 2]
    registers, to_print, jump = opcode_instruct(pair, registers, to_print)
    if jump:
        idx = pair[1]
    else:
        idx += 2

result = ",".join([str(elem) for elem in to_print])
print(f'Advent of Code Day 17 Answer Part 1: {result}')

# Part 2

# my intuition seems to be wrong here, maybe I will revisit this

with open('day17ex2.txt', 'r') as file:
    #for line in file:
    #    line = line.strip('\n')
    registers, instructions = file.read().split("\n\n")
    registers = [int(elem) for elem in re.findall("\d+", registers)]
    registers = dict(zip(["A", "B", "C"], registers))
    instructions = [int(elem) for elem in re.findall("\d+", instructions)]

# opcodes, operands
instruct = zip(instructions[::2], instructions[1::2])
orig_registers = deepcopy(registers)

"""
Pattern:

    Note: increments every 8 numbers i.e. it is base 3

    result: 597 | 2,1,1,0
    result: 598 | 2,1,1,0
    result: 599 | 2,1,1,0
    result: 600 | 3,1,1,0
    result: 601 | 3,1,1,0
    result: 602 | 3,1,1,0
    
    i.e.
    
    0,1,0 --> 8**2
    1,1,0 --> 8**1 * 1 + 8**2
    2,1,0 --> 8**1 * 2 + 8**2
    0,2,0 --> 8**2 * 2
    
    ...
    
    0,3,5,4,3,0 --> 8**2 * 3 + 8**3 * 5 + 8**4 * 4 + 8**5 * 2
"""
for i in range(0, 10):
    registers = orig_registers
    registers["A"] = i
    to_print = []
    idx = 0
    while idx < len(instructions):
        pair = instructions[idx:idx + 2]
        registers, to_print, jump = opcode_instruct(pair, registers, to_print)
        if jump:
            idx = pair[1]
        else:
            idx += 2

    result = ",".join([str(elem) for elem in to_print])
    #print(f"result: {i} | {result}")

ins = instructions[:-1]
total = 0
for i, num in enumerate(ins):
    total += num * (8**(i + 1))

# wrong result :(
print(f'Advent of Code Day 17 Answer Part 2: {total}')

print(f"elapsed time: {time.perf_counter() - start_time}")
