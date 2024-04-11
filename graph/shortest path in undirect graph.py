from typing import List
from queue import PriorityQueue
from collections import defaultdict
from typing import List
class Solution:
    def shortestPath(self,n,m,edges):
        # code here
        
        adj = defaultdict(list)
        for nodedetails in edges:
            start,end,weight = nodedetails
            adj[start].append((end,weight))
            
        
        dist = [(float("inf"),-1)]*(n+1)
        
        pq = PriorityQueue()
        pq.put((0,1))
        
        dist[1] = (0,-1)
        while not pq.empty():
            
            weight,parent = pq.get()
            
            for childDetails in adj[parent]:
                childNode,childWeight = childDetails
                localWeight = childWeight+weight
                
                if localWeight<dist[childNode][0]:
                    dist[childNode] = (localWeight,parent)
                    pq.put((localWeight,childNode))
                
        
        if dist[-1][-1]==-1:
            return -1
        
        ind = n
        result = [n]
        while dist[ind][-1]!=-1:
            result.append(dist[ind][-1])
            ind = dist[ind][-1]
        
        # result = result[::-1]
        result.append(dist[-1][0])
        
        return result[::-1]
    

obj = Solution()
n = 5 
m= 6
edges = [[1,2,2], [2,4,5], [2,5,4], [1,4,1],[4,3,3],[3,5,1]]
print(obj.shortestPath(n,m,edges))
                