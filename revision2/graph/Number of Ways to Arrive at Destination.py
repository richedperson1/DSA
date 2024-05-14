#User function Template for python3

from typing import List
from collections import defaultdict,deque
from queue import PriorityQueue
import sys

class customerPQ(PriorityQueue):
    def __len__(self):
        return len(self.queue)
    
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:       
         
        adj = defaultdict(list)
        for start,end,weight in roads:
            adj[start].append([end,weight])
            adj[end].append([start,weight])
            
        
        dist = defaultdict(lambda : float("inf"))
        ways = defaultdict(int)
        
        ways[0] = 1
        dist[0] = 0
        
        dq = customerPQ()
        dq.put([0,0])
        mod = 10**9 + 7
        while len(dq):
            Nweight,node = dq.get()
            for childNode,childWeight in adj[node]:
                totalWeight = childWeight+Nweight
                
                if dist[childNode]>totalWeight:
                    ways[childNode] = ways[node]
                    dist[childNode] = totalWeight
                    dq.put([totalWeight,childNode])
                
                elif dist[childNode]==totalWeight:
                    ways[childNode] = (ways[childNode]+ways[node])%mod
        
        return ways[n-1]%mod

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

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
        mod = 10**9 + 7
        while pq.empty()!=True:
            
            nWeight,node = pq.get()
            
            for childNode,weight in adj[node]:
                
                localWeight = weight+nWeight
                
                if localWeight < dist[childNode]:
                    ways[childNode] = ways[node]
                    dist[childNode] = localWeight
                    pq.put((localWeight,childNode))
                    
                elif localWeight== dist[childNode]:
                    ways[childNode] = (ways[node] +ways[childNode])%mod
                    
        return ways[n-1]%mod

n=7
m=10
edges= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
obj = Solution().countPaths(n,edges)
print(obj)