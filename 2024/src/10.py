from datetime import datetime as dt
from helpers.h10 import *


grid = []

# Read input
t_0 = dt.now()
with open('2024/input/10.txt', 'r') as file:
    for line in file:
        grid.append([])
        [grid[-1].append(int(char)) for char in line if char != '\n']

m, n = len(grid), len(grid[0])

trailhead_positions = []
for i in range(m):
    for j in range(n):
        if grid[i][j] == 0:
            trailhead_positions.append([i, j])

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))


# Part A
sum_trailhead_scores = 0
for i in range(len(trailhead_positions)):
    sum_trailhead_scores += calculate_trailhead_score(grid, trailhead_positions[i], m, n)

print("Part A: {0}".format(sum_trailhead_scores))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
num_trailhead_paths = 0
for i in range(len(trailhead_positions)):
    num_trailhead_paths += calculate_trailhead_score_all_paths(grid, trailhead_positions[i], m, n)

print("Part B: {0}".format(num_trailhead_paths))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))
