import copy
mat = [['O', 'X', 'X', 'X'], 
       ['O', 'O', 'X', 'X'], 
       ['X', 'O', 'O', 'X'], 
       ['X', 'O', 'X', 'O'], 
       ['X', 'X', 'O', 'O']]

mat = [
    ["X","X","X"],
    ["X","O","X"],
    ["X","X","X"],
    ]
def replaceX2O(grid):
    n,m = len(grid),len(grid[0])
    def check(row,col):
        if row not in range(n) or col not in range(m):
            return False    
        return True
    
    def dfs(row,col):
        visit.add((row,col))
    
        local = [[-1,0],[1,0],[0,1],[0,-1]]
            
        for r,c in local:
            newR = row+r
            newC = col+c
            if not check(newR,newC):
                continue
            
            if grid[newR][newC]=="O" and (newR,newC) not in visit:
                dfs(newR,newC)

        return True
        
    
    visit = set()
    col = m-1
    for row in range(n):
        if grid[row][0]=="O":
            dfs(row,0)
        if grid[row][col]=="O":
            dfs(row,col)

    for col in range(m):
        if grid[0][col]=="O":
            dfs(0,col)
        if grid[n-1][col]=="O":
            dfs(n-1,col)

    for row in range(n):
        for col in range(m):
            if (row,col) not in visit and grid[row][col]=="O":
                grid[row][col] = "X"


    return grid


replaceX2O(mat)