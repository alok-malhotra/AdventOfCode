# Part A
UP_LEFT = [-1, -1]
UP = [-1, 0]
UP_RIGHT = [-1, 1]
RIGHT = [0, 1]
DOWN_RIGHT = [1, 1]
DOWN = [1, 0]
DOWN_LEFT = [1, -1]
LEFT = [0, -1]

def search_grid(grid: list[list], i: int, j: int, m: int, n: int, direction: list, next_char: str) -> int:
    if i < 0 or j < 0: return 0
    if i == m or j == n: return 0
    if grid[i][j] == 'S' and next_char == 'S':
        return 1
    elif grid[i][j] == 'A' and next_char == 'A':
        return search_grid(grid, i + direction[0], j + direction[1], m, n, direction, 'S')
    elif grid[i][j] == 'M' and next_char == 'M':
        return search_grid(grid, i + direction[0], j + direction[1], m, n, direction, 'A')
    return 0

def xmases_from_curr_x(grid: list[list], i: int, j: int, m: int, n: int) -> int:
    up_left = search_grid(grid, i-1, j-1, m, n, UP_LEFT, 'M')
    up = search_grid(grid, i-1, j, m, n, UP, 'M')
    up_right = search_grid(grid, i-1, j+1, m, n, UP_RIGHT, 'M')
    right = search_grid(grid, i, j+1, m, n, RIGHT, 'M')
    down_right = search_grid(grid, i+1, j+1, m, n, DOWN_RIGHT, 'M')
    down = search_grid(grid, i+1, j, m, n, DOWN, 'M')
    down_left = search_grid(grid, i+1, j-1, m, n, DOWN_LEFT, 'M')
    left = search_grid(grid, i, j-1, m, n, LEFT, 'M')

    return up_left + up + up_right + right + down_right + down + down_left + left


# Part B
def left_diagonal_spells_mas(grid, i, j):
    return (grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M')

def right_diagonal_spells_mas(grid, i, j):
    return (grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M')

def is_mas_x(grid, i, j, m, n):
    if i-1 < 0 or j-1 < 0: return False
    if i+1 >= m or j+1 == n: return False
    return left_diagonal_spells_mas(grid, i, j) and right_diagonal_spells_mas(grid, i, j)