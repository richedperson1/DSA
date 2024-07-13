from typing import List
from queue import PriorityQueue
from collections import defaultdict

class custom_pq(PriorityQueue):
    
    def __len__(self):
        return self.queue
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        if len(edges)==0:
            return -1
        adj = defaultdict(list)
        
        for data in edges:
            u,v,w = data
            adj[u].append([v,w])
            
        pq = custom_pq()
        dist = defaultdict(lambda : [float("inf"),-1])
        
        dist[1] = [0,-1]
        pq.put([0,1])
        
        while not pq.empty():
            p_weight,p_node = pq.get()

            for child_data in adj[p_node]:
                c_node,c_weight = child_data
                local_weight = c_weight+p_weight
                if dist[c_node][0]>local_weight:
                    dist[c_node] = [local_weight,p_node]
                    pq.put([local_weight,c_node])
        
        result = [n]
        
        ind = n
        while dist[ind][-1]!=-1:
            result.append(dist[ind][-1])
            ind = dist[ind][-1]
        return(result)
        return dist
                  

n = 5 
m = 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]

obj = Solution()

print(obj.shortestPath(n,m,edges))

