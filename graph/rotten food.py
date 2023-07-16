from collections import deque

class Solution:
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])
        rotten = deque()
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    rotten.append((row, col, 0))
        
        total = 0
        while rotten:
            row, col, out = rotten.popleft()
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            for r, c in directions:
                newR = row + r
                newC = col + c
                
                if newR < 0 or newC < 0 or newR >= n or newC >= m:
                    continue
                
                if grid[newR][newC] == 2:
                    continue
                
                if grid[newR][newC] == 1:
                    rotten.append((newR, newC, out + 1))
                    grid[newR][newC] = 2
                    total = max(out + 1, total)

        for col in range(m):
            for row in range(n):
                if grid[row][col]==1:
                    return -1
        return total


element = '''0 1 2 
0 1 0
2 0 1'''

grid = [list(map(int,data.split())) for data in element.split('\n')]


obj = Solution()
print(obj.orangesRotting(grid))