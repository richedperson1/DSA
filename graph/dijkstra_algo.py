from queue import PriorityQueue
class Solution:
    def dijkstra(self, v, adj, s):
        #code here
        
        dist = [float('inf')]*v

        dist[s] = 0
        
        pq = PriorityQueue()
        pq.put((0,s))
        while not pq.empty():
            weight,node = pq.get()
            
            for childsDetails in adj[node]:
                child,cweight = childsDetails
                new_weight    = weight+cweight
                if new_weight<dist[child]:
                    dist[child] = new_weight
                    pq.put((new_weight,child))
        
        return dist
        
obj = Solution()

v = 2
adj = [[(1,9)],[(0,9)]]
s = 0
print(obj.dijkstra(v,adj,s))