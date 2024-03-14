from collections import deque
class Solution:
    
    """
    The function `orangesRotting` implements a breadth-first search algorithm to determine the maximum
    time taken for all oranges in a grid to rot, with each minute causing adjacent fresh oranges to rot
    as well.
    
    :param grid: It looks like you have provided a code snippet for a function that performs a BFS
    (Breadth-First Search) traversal on a grid to simulate the rotting of oranges. The function seems to
    be incomplete, but I can help you understand and complete it
    """
    
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