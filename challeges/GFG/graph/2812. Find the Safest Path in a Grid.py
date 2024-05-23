from collections import deque
from queue import PriorityQueue
from typing import List

class customerPQ(PriorityQueue):
    def __len__(self):
        return self.queue
    def __repr__(self):
        return f"{self.queue}"
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        self.score = [[float("inf")]*cols for _ in range(cols)]
        dire = [[1,0],[0,1],[-1,0],[0,-1]]
        def bfs():
            dq = deque()
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col]==1:
                        self.score[row][col] = 0
                        dq.append((row,col))

            
            while len(dq):
                nRow,nCol = dq.popleft()
                score = self.score[nRow][nCol]
                for dRow,dCol in dire:
                    newRow = nRow + dRow
                    newCol = nCol + dCol
                    if(newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and self.score[newRow][newCol] > 1 + score):
                        dq.append((newRow,newCol))
                        self.score[newRow][newCol] = 1+score
        
        bfs()
        print(self.score)
        pq = customerPQ()
        first = -self.score[0][0]
        # print(first)
        pq.put((first,0,0))
        visit = {}
        visit[(0,0)] = True
        while not pq.empty():
            scoring,nRow,nCol = pq.get()
            scoring = abs(scoring)
            
            if nRow==(rows-1) and nCol==(cols-1):
                return scoring
            
            for dRow,dCol in dire:
                newRow = nRow+dRow
                newCol = nCol+dCol
                if(newRow >= 0 and newRow < rows and newCol >= 0 and newCol < cols and visit.get((newRow,newCol),False)==False ):
                    s = min(scoring,self.score[newRow][newCol])
                    # print(scoring)
                    pq.put((-s,newRow,newCol))
                    visit[(newRow,newCol)]  =  True
        
                
            
obj = Solution()
grid = [[1,0,0],[0,0,0],[0,0,1]]
grid = [[0,0,1],[0,0,0],[0,0,0]]
grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
grid = [[0,1,1],[0,0,1],[1,0,0]]

print(obj.maximumSafenessFactor(grid))
