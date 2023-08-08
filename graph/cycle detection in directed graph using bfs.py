from typing import List
from collections import defaultdict
import sys
sys.setrecursionlimit(10**9) 
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here

        def dfsCall(node):
            isCheck[node] = False
            isPath[node] = True
            visit[node] = True
            for child in adj[node]:
                if not visit[child]:
                    ans = dfsCall(child)
                    if ans:
                        return True
                        
                elif isPath[child]:
                    return True
                    
            isPath[node] = False
            isCheck[node] = True
            return False
            
        visit = defaultdict(bool)
        isCheck = defaultdict(bool)
        isPath = defaultdict(bool)
        for v in range(V):
            if not visit[v]:
                dfsCall(v)
         
         
        ans = []       
        
        for key in range(V):
            if isCheck[key]:
                ans.append(key)
                
        return ans