def i_in_bounds(i: int, m: int) -> bool:
    return i >= 0 and i < m

def j_in_bounds(j: int, n: int) -> bool:
    return j >= 0 and j < n

def pos_in_bounds(i: int, j: int, m: int, n: int) -> bool:
    return i_in_bounds(i, m) and j_in_bounds(j, n)

def calculate_trailhead_score(grid: list[list], starting_position: list, m: int, n: int) -> int:
    nine_set = set()
    
    trail_search(grid, 1, starting_position[0] + 1, starting_position[1], m, n, nine_set)
    trail_search(grid, 1, starting_position[0] - 1, starting_position[1], m, n, nine_set)
    trail_search(grid, 1, starting_position[0], starting_position[1] + 1, m, n, nine_set)
    trail_search(grid, 1, starting_position[0], starting_position[1] - 1, m, n, nine_set)

    return len(nine_set)

def trail_search(grid: list[list], curr_val: int, i: int, j: int, m: int, n: int, nine_set: set) -> None:
    if not pos_in_bounds(i, j, m, n): 
        return
    if grid[i][j] != curr_val: return
    if grid[i][j] == 9 and curr_val == 9:
        nine_set.add((i, j))
        return
    trail_search(grid, curr_val + 1, i+1, j, m, n, nine_set)
    trail_search(grid, curr_val + 1, i-1, j, m, n, nine_set)
    trail_search(grid, curr_val + 1, i, j-1, m, n, nine_set)
    trail_search(grid, curr_val + 1, i, j+1, m, n, nine_set)

def calculate_trailhead_score_all_paths(grid: list[list], starting_position: list, m: int, n: int) -> int:
    return trail_search_all_paths(grid, 1, starting_position[0] + 1, starting_position[1], m, n) \
            + trail_search_all_paths(grid, 1, starting_position[0] - 1, starting_position[1], m, n) \
            + trail_search_all_paths(grid, 1, starting_position[0], starting_position[1] + 1, m, n) \
            + trail_search_all_paths(grid, 1, starting_position[0], starting_position[1] - 1, m, n)

def trail_search_all_paths(grid: list[list], curr_val: int, i: int, j: int, m: int, n: int) -> int:
    if not pos_in_bounds(i, j, m, n): 
        return 0
    if grid[i][j] != curr_val: return 0
    if grid[i][j] == 9 and curr_val == 9:
        return 1
    return trail_search_all_paths(grid, curr_val + 1, i+1, j, m, n) \
            + trail_search_all_paths(grid, curr_val + 1, i-1, j, m, n) \
            + trail_search_all_paths(grid, curr_val + 1, i, j-1, m, n) \
            + trail_search_all_paths(grid, curr_val + 1, i, j+1, m, n)
