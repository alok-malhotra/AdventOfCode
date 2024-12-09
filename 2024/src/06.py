from datetime import datetime as dt
from helpers.h06 import *


grid = []
UP, LEFT, DOWN, RIGHT = 1, 2, 3, 4

# Read input
t_0 = dt.now()
with open('2024/input/6.txt', 'r') as file:
    for line in file:
        grid.append([])
        [grid[-1].append(char) for char in line if char != '\n']

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

m, n = len(grid), len(grid[0])
# Part A
i, j = locate_start(grid, m, n)
direction = UP

while True:
    if i_out_of_range(i, m) or j_out_of_range(j, n):
        break
    grid[i][j] = 'X'

    if direction == UP:
        if grid[i-1][j] == '#':
            direction = RIGHT
        else: 
            i -= 1
    elif direction == DOWN:
        if grid[i+1][j] == '#':
            direction = LEFT
        else: 
            i += 1
    elif direction == RIGHT:
        if grid[i][j+1] == '#':
            direction = DOWN
        else: 
            j += 1
    else: # LEFT
        if grid[i][j-1] == '#':
            direction = UP
        else: 
            j -= 1

num_x = count_x(grid, m, n)

print("Part A: {0}".format(num_x))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
# IMPLEMENT HERE


print("Part B: {0}".format("<INSERT HERE>"))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))