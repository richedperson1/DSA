
from typing import List
from collections import deque,defaultdict
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        # code here
        
        dq = deque([(0,source[0],source[1])])
        
        dire = [[0,1],[1,0],[-1,0],[0,-1]]
        rows,cols = len(grid),len(grid[0])
        visit = defaultdict()
        while len(dq)>0:
            steps,pRow,pCol = dq.popleft()
            if pRow==destination[0] and pCol ==destination[1]:
                return steps
            for dirR,dirC in dire:
                newCol = pCol+dirC
                newRow = pRow+dirR
                
                if 0<=newRow< rows and 0<=newCol < cols and grid[newRow][newCol]==1 and (newRow,newCol) not in visit:
                    visit[(newRow,newCol)] = True
                    dq.append((steps+1,newRow,newCol))

        return -1
    
obj = Solution()
grid = [[1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 1]]
source = [0, 1]
destination = [2, 2]
print(obj.shortestPath(grid,source,destination))