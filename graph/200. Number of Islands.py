def bfs(r, c, grid, visit):
    row = len(grid)
    col = len(grid[0])
    if (r >= row or c >= col) or (r < 0 or c < 0):
        return 0

    try:
        if grid[r][c] == "1" and (r, c) not in visit:

            visit.add((r, c))
            bfs(r+1, c, grid, visit)
            bfs(r-1, c, grid, visit)
            bfs(r, c+1, grid, visit)
            bfs(r, c-1, grid, visit)
        else:
            return 0
    except:
        print(r, c)
        raise


def numIslands(grid: list[list[str]]) -> int:
    row = len(grid)
    col = len(grid[0])

    visit = set()

    totalIland = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c, grid, visit)
                totalIland += 1

    return totalIland


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(numIslands(grid))
