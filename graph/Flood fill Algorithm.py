import sys
sys.setrecursionlimit(10**9)
class Solution:
    def floodFill(self,img,sr,sc,new_color):
        result = [data for data in img]
        
        
        main_color = result[sr][sc]
        visit = {}
        result[sr][sc] = new_color
        visit[(sr,sc)] = True
        def dfs(sr,sc):
            nonlocal result
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            for row,col in direction:
                new_r = row+sr
                new_c = col+sc
                
                if (not(new_r>=len(grid) or new_c>= len(grid[0]) or new_r<0 or new_c<0)) and result[new_r][new_c]==main_color and (new_r,new_c) not in visit:
                    # continue
                    visit[(new_r,new_c)] = True
                    result[new_r][new_c] = new_color
                    dfs(new_r,new_c)
        dfs(sr,sc)
        # print(result)
        return result

grid = [[2, 3, 2, 1, 2], [3, 3, 3, 3, 1], [3, 1, 1, 1, 2], [1, 2, 2, 1, 3], [1, 2, 3, 3, 1], [2, 1, 2, 2, 2], [1, 2, 2, 1, 1], [3, 1, 1, 1, 2]]
obj = Solution()
row,col,new = 4,0,1
print(obj.floodFill(grid,row,col,new))