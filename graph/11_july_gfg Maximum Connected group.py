from typing import List

class disjoint:
    def __init__(self,rows,cols):
        self.parent = [ind for ind in range(rows*cols)]
        self.size  = [1 for ind in range(rows*cols)]
        self.rows = rows
        self.cols = cols
    
    def flatten_val(self,row,col):
        return row*self.cols+col
        
    def find_parent(self,nodes):
        
        # index = self.flatten_val(row,col)
        
        def _parent_find(self,node):
            if self.parent[node]==node:
                return node
                
            self.parent[node] = _parent_find(self,self.parent[node])
            return self.parent[node]
            
        return _parent_find(self,nodes)
            
    def unionBySize(self,parA,parB):
        
        ultA = self.find_parent(parA)
        ultB = self.find_parent(parB)
        
        if ultA==ultB:
            return None
            
        
        elif self.size[ultA]>self.size[ultB]:
            self.size[ultA]+= self.size[ultB]
            self.parent[ultB] = ultA
        
        else:
            self.size[ultB]+= self.size[ultA]
            self.parent[ultA] = ultB
    
class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        # dp = [[0 for col in range(cols)] for row in range(rows)]
        dire = [[1,0],[0,1],[-1,0],[0,-1]]
        dis = disjoint(rows,cols)
        def dfs(row,col):
            for dr,dc in dire:
                new_r = row+dr
                new_c = col+dc
                # if rows>new_r >=0 and cols>col>=0 and present.get((new_r,new_c),False)==False:
                if rows> new_r >=0 and cols>new_c>=0:
                    if grid[new_r][new_c]==1:
                        index_c = dis.flatten_val(new_r,new_c)
                        index_p = dis.flatten_val(row,col)
                        dis.unionBySize(index_c,index_p)
                        present[(new_r,new_c)] = 1
                        
                parent = dis.parent
                size = dis.size
        present = {}
        zero_present = {}
        # dis = disjoint(rows,cols)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and present.get((row,col),-2)==-2:
                    dfs(row,col)
                    present[(row,col)] = 1
                elif grid[row][col]==0:
                    zero_present[(row,col)] = 1
        
        print(dis.size)
        print(dis.parent)
        
        
        def zero_point(row,col):
            maxi = 0
            size1 = dis.size
            zePre = {}
            for dr,dc in dire:
                new_r = row+dr
                new_c = col+dc
                if rows> new_r >=0 and cols>new_c>=0 :
                    index_c = dis.flatten_val(new_r,new_c)
                    if grid[new_r][new_c]==1 and zePre.get(index_c,-4)==-4:
                        ultC = dis.find_parent(index_c)
                        maxi+=dis.size[ultC]
                        zePre[ultC] = 1
            return maxi
                        
        final_ans = 0
        
        for data in zero_present:
            row0,col0 = data
            
            local = zero_point(row0,col0)+1
            final_ans = max(final_ans,local)
            
        return final_ans
    
                    

        
        
    
# grid = [[1, 0, 1],[1, 0, 1],[1, 0, 1]]
grid = [[1, 0],[1, 1]]


grid = [[1, 0, 0, 1], 
        [1, 0, 1, 0], 
        [1, 0, 1, 0], 
        [1, 1, 0, 1]]

obj1 = Solution()

print(obj1.MaxConnection(grid))