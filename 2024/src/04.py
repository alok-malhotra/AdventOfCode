from datetime import datetime as dt
from helpers.h04 import *


grid = []

# Read input
t_0 = dt.now()
with open('2024/input/4.txt', 'r') as file:
    for line in file:
        grid.append([])
        for char in line: 
            if char != '\n': grid[-1].append(char)

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

m, n = len(grid), len(grid[0])
# Part A
num_xmases = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'X':
            num_xmases += xmases_from_curr_x(grid, i, j, m, n)

print("Part A: {0}".format(num_xmases))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
num_mas_x = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'A':
            if is_mas_x(grid, i, j, m, n): num_mas_x += 1

print("Part B: {0}".format(num_mas_x))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
