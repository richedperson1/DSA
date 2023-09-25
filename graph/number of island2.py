#User function Template for python3
from typing import *
class disjoint:
    def __init__(self,v):
        self.rank = [0]*v
        self.parent = [ind for ind in range(v)]
        
    def findParent(self,u):
        if self.parent[u]==u:
            return u
        
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
        
    
    def unionByRank(self,u,v):
        ultU = self.findParent(u)
        ultV = self.findParent(v)
        
        if ultU==ultV:
            return 
        
        if self.rank[ultU]>self.rank[ultV]:
            self.parent[ultV] = ultU
        
        elif self.rank[ultU]<self.rank[ultV]:
            self.parent[ultU] = ultV
            
        else:
            self.parent[ultV] = ultU
            self.rank[ultU]+=1
            
            
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        
        def valid(row,col):
            return row<rows and col<cols and col>=0 and row>=0
        total = rows*cols
        dis = disjoint(total)
        ans = []
        vis = [[[0] for ind in range(cols)] for col in range(rows)]
        cnt = 0
        for data in operators:
            rowI,colI = data
            if vis[rowI][colI]==1:
                ans.append(cnt)
                continue
            vis[rowI][colI]=1
            cnt+=1
            
            
            dire = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in dire:
                newR, newC = dr+rowI,dc+colI
                
                if valid(newR,newC):
                    if vis[newR][newC]==1:
                        adjI  = newC + newR*cols
                        nodeI = colI + rowI*cols
                        if dis.findParent(nodeI)!=dis.findParent(adjI):
                            cnt-=1
                            dis.unionByRank(adjI,nodeI)
            
            ans.append(cnt)
        return ans
            