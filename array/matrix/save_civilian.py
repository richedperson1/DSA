n = 5
m = 5
E = "E"
C = "C"
T = "T"
grid = [
    [E, E, E, C, E],
    [E, E, C, C, E],
    [E, C, E, E, E],
    [E, E, T, T, E],
    [E, E, E, E, E]
]

grid = [[T, T], [E, C]]


def check(grid, row, col):
    n, m = len(grid), len(grid[0])

    if row+1 < n and grid[row+1][col] == "C":
        return False
    if row < n and col+1 < m and grid[row][col+1] == 'C':
        return False

    if row-1 >= 0 and grid[row-1][col] == "C":
        return False
    if row and col-1 >= 0 and grid[row][col-1] == "C":
        return False

    return True


def saveCivilians(grid):
    n, m = len(grid), len(grid[0])
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "T":
                if check(grid, row, col) == False:
                    return False
    return True


print(saveCivilians(grid))
