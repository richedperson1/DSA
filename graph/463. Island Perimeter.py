"""
URL : https://leetcode.com/problems/island-perimeter/
"""
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


def checkSide(grid, row, col, total):

    rows = len(grid)
    cols = len(grid[0])

    if row+1 >= rows or grid[row+1][col] == 0:
        total += 1

    if row-1 < 0 or grid[row-1][col] == 0:
        total += 1

    if col-1 < 0 or grid[row][col-1] == 0:
        total += 1

    if col+1 >= cols or grid[row][col+1] == 0:
        total += 1

    return total


def CalculateArea(grid):
    totalNum = 0

    def dfs(row, col, visited):
        nonlocal totalNum
        visited[(row, col)] = True
        if visited.get((row, col), False):
            return 0
        if row >= rows or col >= cols:
            return 0
        totalNum += checkSide(grid, row, col, 0)
        dfs(row+1, col, visited)
        dfs(row+1, col+1, visited)
        dfs(row+1, col+1, visited)
        dfs(row+1, col+1, visited)

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            # if visited.get((row, col), -1) == -1 and grid[row][col] != 0:
            if grid[row][col] != 0:
                totalNum += checkSide(grid, row, col, 0)

    return totalNum


print(CalculateArea(grid))
