import sys
sys.setrecursionlimit(10**9)
class Solution:
    def numIslands(self,grid):
        #code here
        visit = {}
        
        def dfs(row,col):
            # if row>=len(grid) or col>= len(grid[0]) or row<0 or col<0:
            #     return 0
            for rs,cs in [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,-1],[-1,1],[-1,0]]:
                new_r = row+rs
                new_c = col+cs
                if (new_r,new_c) in visit or (new_r>=len(grid) or new_c>= len(grid[0]) or new_r<0 or new_c<0) or grid[new_r][new_c]==0:
                    continue
                
                visit[(new_r,new_c)] = True
                dfs(new_r,new_c)
        
        rows = len(grid)
        cols = len(grid[0])
        total = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and visit.get((row,col),-2)==-2:
                    total+=1
                    print(row,col)
                    dfs(row,col)
                    print(visit)
        # print(visit)
        return total
    

obj = Solution()
# grid = [[0, 1], [1, 0], [1, 1], [1, 0]]
grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
print(obj.numIslands(grid))