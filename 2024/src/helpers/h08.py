def i_pos_on_grid(i: int, m: int) -> bool:
    return i >= 0 and i < m

def j_pos_on_grid(j: int, n: int) -> bool:
    return j >= 0 and j < n

def point_on_grid(i: int, j: int, m: int, n: int) -> bool:
    return i_pos_on_grid(i, m) and j_pos_on_grid(j, n)

def calculate_points_deltas(point_one: list, point_two: list) -> list:
    return [ point_one[0] - point_two[0], point_one[1] - point_two[1] ]

def get_antinodes_for_antenna_id(positions: list[list], m: int, n: int) -> list[list]:
    antinodes = []
    
    for i in range(len(positions)):
        for j in range(i):
            position_one, position_two = positions[i], positions[j]
            deltas = calculate_points_deltas(position_one, position_two)
            antinode_one = [position_one[0] + deltas[0], position_one[1] + deltas[1]]
            if antinode_one == position_two:
                deltas = [-1 * deltas[i] for i in range(len(deltas))]
                antinode_one = [position_one[0] + deltas[0], position_one[1] + deltas[1]]
            antinode_two = [position_two[0] + deltas[0], position_two[1] + deltas[1]]
            if antinode_two == position_one:
                deltas = [-1 * deltas[i] for i in range(len(deltas))]
                antinode_two = [position_two[0] + deltas[0], position_two[1] + deltas[1]]
            if point_on_grid(antinode_one[0], antinode_one[1], m, n):
                antinodes.append(antinode_one)
            if point_on_grid(antinode_two[0], antinode_two[1], m, n):
                antinodes.append(antinode_two)
    return antinodes

def get_antinodes_for_antenna_id_with_resonance(positions: list[list], m: int, n: int) -> list[list]:
    antinodes = []
    
    for i in range(len(positions)):
        for j in range(i):
            position_one, position_two = positions[i], positions[j]
            deltas = calculate_points_deltas(position_one, position_two)
            
            antinode_d1_one = [position_one[0] + deltas[0], position_one[1] + deltas[1]]
            while point_on_grid(antinode_d1_one[0], antinode_d1_one[1], m, n):
                antinodes.append(antinode_d1_one)
                antinode_d1_one = [antinode_d1_one[0] + deltas[0], antinode_d1_one[1] + deltas[1]]

            antinode_d2_one = [position_one[0] - deltas[0], position_one[1] - deltas[1]]
            while point_on_grid(antinode_d2_one[0], antinode_d2_one[1], m, n):
                antinodes.append(antinode_d2_one)
                antinode_d2_one = [antinode_d2_one[0] - deltas[0], antinode_d2_one[1] - deltas[1]]

            antinode_d1_two = [position_two[0] + deltas[0], position_two[1] + deltas[1]]
            while point_on_grid(antinode_d1_two[0], antinode_d1_two[1], m, n):
                antinodes.append(antinode_d1_two)
                antinode_d1_two = [antinode_d1_two[0] + deltas[0], antinode_d1_two[1] + deltas[1]]

            antinode_d2_two = [position_two[0] - deltas[0], position_two[1] - deltas[1]]
            while point_on_grid(antinode_d2_two[0], antinode_d2_two[1], m, n):
                antinodes.append(antinode_d2_two)
                antinode_d2_two = [antinode_d2_two[0] - deltas[0], antinode_d2_two[1] - deltas[1]]

    return antinodes