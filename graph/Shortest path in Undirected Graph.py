
from collections import defaultdict,deque
from queue import PriorityQueue
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adj = defaultdict(list)
        
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
            
        
        dq = PriorityQueue()
        dist = [float("inf")]*n
        
        dq.put((0,src))
        dist[src] = 0
        
        
        while not dq.empty():
            weight,pnode = dq.get()
            
            for child in adj[pnode]:
                if weight+1<dist[child]:
                    dist[child] = weight+1
                    dq.put((weight+1,child))
        
        
        for ind,data in enumerate(dist):
            if data==float("inf"):
                dist[ind] = -1
                
        return dist
    
arr = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6], [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]

obj = Solution()
n = 9
m = len(arr)

print(obj.shortestPath(arr,n,m,0))



# 13 12 14 5 N N N 1 7 N 2 6 11 N 4 N N 8 N 3 N N 9 N N N 10 N N