from datetime import datetime as dt
from helpers.h08 import *

grid = []

# Read input
t_0 = dt.now()
with open('2024/input/8.txt', 'r') as file:
    for line in file:
        grid.append([])
        [grid[-1].append(char) for char in line if char != '\n']

t_a_s = dt.now()
reading_input_completion_time = (t_a_s - t_0).total_seconds()
print("Reading input took: {0} seconds\n".format(reading_input_completion_time))

m, n = len(grid), len(grid[0])
# Part A
antenna_positions = {}
for i in range(m):
    for j in range(n):
        char = grid[i][j]
        if char != ".":
            antenna_positions[char] = antenna_positions.get(char, [])
            antenna_positions[char].append([i, j])

antinode_positions = set()
antinode_positions_by_id = {}
for antenna_id, positions in antenna_positions.items():
    antinodes_for_antenna_id = get_antinodes_for_antenna_id(positions, m, n)

    antinode_positions_by_id[antenna_id] = antinode_positions_by_id.get(antenna_id, [])
    antinode_positions_by_id[antenna_id].append(antinodes_for_antenna_id)
    
    for antinode in antinodes_for_antenna_id:
        antinode_positions.add((antinode[0], antinode[1]))

print("Part A: {0}".format(len(antinode_positions)))
t_a_e = dt.now()
part_a_completion_time = (t_a_e - t_a_s).total_seconds()
print("Time for Part A: {} seconds\n".format(part_a_completion_time))


# Part B
t_b_s = dt.now()
antinode_positions_with_resonance = set()
antinode_positions_by_id_with_resonance = {}
for antenna_id, positions in antenna_positions.items():
    antinodes_for_antenna_id = get_antinodes_for_antenna_id_with_resonance(positions, m, n)

    antinode_positions_by_id_with_resonance[antenna_id] = antinode_positions_by_id_with_resonance.get(antenna_id, [])
    antinode_positions_by_id_with_resonance[antenna_id].append(antinodes_for_antenna_id)
    
    for antinode in antinodes_for_antenna_id:
        antinode_positions_with_resonance.add((antinode[0], antinode[1]))


print("Part B: {0}".format(len(antinode_positions_with_resonance)))
t_b_e = dt.now()
part_b_completion_time = (t_b_e - t_b_s).total_seconds()
print("Time for Part B: {} seconds\n".format(part_b_completion_time))