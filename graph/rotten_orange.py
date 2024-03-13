from collections import deque
class Solution:
    def orangesRotting(self,grid):
        rows = len(grid)
        cols = len(grid[0])
        
        dq = deque([])
        self.total = 0
        visit = {}
        
        def bfs():
            size = len(dq)
            
            while dq :
                size = len(dq)
                for ind in range(size):
                    sr,sc,level = dq.popleft()
                    self.total = max(self.total,level)
                    dire = [[0,1],[1,0],[0,-1],[-1,0]]
                    
                    for row,col in dire:
                        new_r = sr+row
                        new_c = sc+col
                        
                        if new_r<0 or new_c<0 or new_r>=rows or new_c>=cols or grid[new_r][new_c]==0  or (new_r,new_c) in visit:
                            continue
                    
                        grid[new_r][new_c] = 2
                        visit[(new_r,new_c)] = True
                        dq.append((new_r,new_c,level+1))
                # self.total+=1
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2:
                    visit[(row,col)] = True
                    dq.append((row,col,0))
        bfs()        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1
        return self.total
    
grid = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]

obj = Solution()
print(obj.orangesRotting(grid))