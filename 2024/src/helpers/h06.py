def locate_start(grid: list[list], m: int, n: int) -> tuple:
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '^':
                return (i, j)
    return "ERROR"

def i_out_of_range(i: int, m: int) -> bool:
    return i < 0 or i >= m

def j_out_of_range(j: int, n: int) -> bool:
    return j < 0 or j >= n

def count_x(grid: list[list], m: int, n: int) -> int:
    x = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'X':
                x += 1
    return x