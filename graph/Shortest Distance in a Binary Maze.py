"""
! URL : https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
"""
from typing import List
import sys
from collections import deque

sys.setrecursionlimit(10**9)
def shortestPath1( grid, source, dest):
    # code here
    if grid[dest[0]][dest[1]] == 0:
        return -1
    
    visit = set()
    def dfs(r,c):
        if (r>=row or r<0 or c>=col or c<0):
            return sys.maxsize
        
        if grid[r][c]==0:
            return sys.maxsize
    
        if r==dest[0] and c== dest[1]:
            return 0
        if dp[r][c]!=-1:
            return dp[r][c]
        
        if (r,c) in visit:
            return sys.maxsize
        
            
    
        
        dire = [[-1,0],[1,0],[0,1],[0,-1]]
        
        ans = sys.maxsize
        visit.add((r,c))
        for dr,dc in dire:
            newR,newC = r+dr,c+dc
            
            local = dfs(newR,newC)+1
            ans = min(ans,local)
            
        dp[r][c] = ans  
        return ans
    
    row = len(grid)
    col = len(grid[0])
    dp = [[-1]*col ]*row
    # print(dp)
    
    ans =  dfs(source[0],source[1])
    return ans


def shortestPath2( grid, source, dest) -> int:
    if grid[dest[0]][dest[1]] == 0:
        return -1
    visit = set()
    
    def dfs(r, c):
        if r >= row or r < 0 or c >= col or c < 0:
            return sys.maxsize
        
        if grid[r][c] == 0:
            return sys.maxsize
        
        if r == dest[0] and c == dest[1]:
            return 0
            
        if dp[r][c] != -1:
            return dp[r][c]
    
        if (r, c) in visit:
            return sys.maxsize
        
        dire = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        ans = sys.maxsize
        visit.add((r, c))
        for dr, dc in dire:
            newR, newC = r + dr, c + dc
            
            local = dfs(newR, newC) + 1
            ans = min(ans, local)
            
        dp[r][c] = ans  
        return ans
    
    row = len(grid)
    col = len(grid[0])
    dp = [[-1] * col for _ in range(row)]  # Initialize dp array correctly
    
    ans = dfs(source[0], source[1])
    if ans >= sys.maxsize:
        return -1
    return ans

# grid =     [[1, 1, 1, 1],
#             [1, 1, 0, 1],
#             [1, 1, 1, 1],
#             [1, 1, 0, 0],
#             [1, 0, 0, 1]]

# grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 0, 1]]


# source = [0, 0]
# destination = [4, 4]
# destination = [3, 4]

def shortestPath(grid, source, dest):
    if grid[dest[0]][dest[1]] == 0:
        return -1

    row, col = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    queue = deque([(source[0], source[1], 0)])  # (row, col, distance)
    visited = set([(source[0], source[1])])

    while queue:
        r, c, distance = queue.popleft()

        if r == dest[0] and c == dest[1]:
            return distance

        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                visited.add((new_r, new_c))
                queue.append((new_r, new_c, distance + 1))

    return -1




grid = [[1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 1]]

grid = [[1,0,1,1,0],
        [1,0,0,1,1],
        [1,1,1,0,1],
        [0,0,1,1,1]]
source = [0, 0]
destination = [0, 2]
n,m = len(grid),len(grid[0])
dist = [[float("inf")]*n for ind in range(m)]
print(dist)
# print(shortestPath(grid,source,destination))
# print(shortestPath1(grid,source,destination))