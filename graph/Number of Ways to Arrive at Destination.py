#User function Template for python3

from typing import List
from collections import defaultdict
from queue import PriorityQueue
# from queue import PriorityQueue

import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #Your code here
        
        adj = defaultdict(list)
        
        for dataNode in roads:
            src,dest,weight = dataNode
            
            adj[src].append((dest,weight))
            adj[dest].append((src,weight))
        pq = PriorityQueue()
        pq.put((0,0))
        
        dist = defaultdict(lambda : float("inf"))
        ways = defaultdict(int)
        ways[0] = 1
        dist[0] = 0
        # print(ways)
        while pq.empty()!=True:
            
            nWeight,node = pq.get()
            
            for childNode,weight in adj[node]:
                
                localWeight = weight+nWeight
                
                if localWeight < dist[childNode]:
                    ways[childNode] = ways[node]
                    dist[childNode] = localWeight
                    pq.put((localWeight,childNode))
                    
                elif localWeight== dist[childNode]:
                    ways[childNode] = ways[childNode]+ ways[node]
                    
        # print(ways)
        return ways[n-1]
            



roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
n = 7 

obj = Solution()
print(obj.countPaths(n,roads))
