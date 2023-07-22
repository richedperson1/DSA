

from collections import deque

def nearest( grid):
    rows = len(grid)
    cols = len(grid[0])
    
    newgrid = [[0]*cols for row in range(rows)]
    visit = set()
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==1:
                visit.add((row,col))
                queue.append((row,col,0))
                # newgrid[row][col] = 0
    
    while queue:
        row,col, step = queue.popleft()
        
        toGo = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for goStep in toGo:
            newRow = row + goStep[0]
            newCol = col + goStep[1]
            
            if  (newRow,newCol) not in visit and (newRow in range(rows) and newCol in range(cols)) and grid[newRow][newCol]!=1:
                visit.add((newRow,newCol))
                newgrid[newRow][newCol] = step+1
                queue.append((newRow,newCol,step+1))
            
    return newgrid


grid = """1 0 1
1 1 0
1 0 0"""

grid = """1 0 1
0 0 0
0 0 0
0 1 0"""
grid = [list(map(int,(obj.split()))) for obj in list(map(str,grid.split('\n')))]
print(grid)
print(nearest(grid))