
def numberOfEnclaves( grid: list[list[int]]) -> int:
    # code here

    def dfs(row,col):
        if not(row in range(rows) or col in range(cols)):
            return False
        
        visit.add((row,col))
        local = [[0,1],[0,-1],[-1,0],[1,0]]
        
        for r,c in local:
            newR = row+r
            newC = col+c
            
            if  (newR in range(rows) and newC in range(cols)) and ((newR,newC) not in visit) and grid[newR][newC]==1:
                dfs(newR,newC)
                
            
    rows,cols = len(grid),len(grid[0])
    visit = set()
    
    for row in range(rows):
        if grid[row][0]==1:
            dfs(row,0)
        if grid[row][cols-1]==1:
            dfs(row,cols-1)
        
    for col in range(cols):
        if grid[0][col]==1:
            dfs(0,col)
        if grid[rows-1][col]==1:
            dfs(rows-1,col)
            
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==1 and (row,col) not in visit:
                count+=1
    return count


arr = """0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0"""

grid = [list(map(int,data.split())) for data in arr.split('\n')]
print(numberOfEnclaves(grid))
