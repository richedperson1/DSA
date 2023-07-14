def numIslands(grid):
    
    def dfs(row,col):
        if row<0 or col <0 or row>=n or col>=m:
            return 0
        if (row,col) in visit or grid[row][col]==0:
            return 0
            
        visit.add((row,col))
        
        for r in range(-1,2):
            for c in range(-1,2):
                newRow = row+r
                newCol = col+c
                if newRow< 0 or newCol < 0 or newRow>=n or newCol>=m:
                    continue
                if (row+r,col+c) not in visit  and grid[newRow][newCol]==1:
                    dfs(row+r,col+c)
    #code here
    n = len(grid)
    m = len(grid[0])
    visit = set()
    count = 0
    for row in range(n):
        for col in range(m):
            once = grid[row][col]
            if ((row,col) not in visit) and (grid[row][col]==1):
                # visit.add((row,col))
                dfs(row,col)
                count +=1
                print(visit)
    print(count)
    return count

# grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
# grid = [[0,1],[1,0],[1,1],[1,0]]
element = '''0 0 1 0 1
1 1 0 1 0
0 0 1 1 0
0 0 1 1 0'''

grid = [list(map(int,data.split())) for data in element.split('\n')]
numIslands(grid)
