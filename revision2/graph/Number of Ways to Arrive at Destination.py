#User function Template for python3

from typing import List
from collections import defaultdict,deque
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        
        adj = defaultdict(list)
        
        for start,end,weight in roads:
            adj[start].append([end,weight])
            
        
        dist = defaultdict(list)
        
        dq = deque()
        dq.append([0,0])
        
        current = defaultdict(lambda :float("inf"))
        print(adj)
        current[0] = 0
        print(dq)
        while len(dq)>0:
            weight,node = dq.popleft()
            print(weight,node)
            if node==n-1:
                dist[weight].append(node)
            
            for child in adj[node]:
                
                cnode,cweight = child
                
                if cweight+weight>current[cnode]:
                    current[cnode] = cweight+weight
                    dq.append([cweight+weight, cnode])
        
        
        print(dist)
    
n = 7

n=7
m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
obj = Solution().countPaths(n,edges)
print(obj)