from collections import defaultdict
import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        
        looping  = defaultdict(bool)
        evaluate = defaultdict(bool)
        visit = defaultdict(bool)
        def dfs(node):
            looping[node] = True
            
            for child in adj[node]:
                if child not in visit:
                    visit[child]  = True
                    local = dfs(child)
                    if local:
                        evaluate[child] = True
                        return True
                
                elif looping[child]:
                    evaluate[child] = True
                    return True
                    
            looping[node] = False
            
            return False
        
        for vtx in range(V):
            if visit.get(vtx,False)==False:
                visit[vtx] = True
                dfs(vtx)
                
        
        ans = []
        for vtx in range(V):
            if evaluate.get(vtx,False)!=True:
                ans.append(vtx)
        return ans

grid = [[1, 2], [2, 3], [5], [0], [5], [], []]
v = len(grid)
obj = Solution().eventualSafeNodes(v,grid)

print(obj)
