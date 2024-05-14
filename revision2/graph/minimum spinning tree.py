from queue import PriorityQueue 

from collections import defaultdict
class customerPQ(PriorityQueue):
    def __len__(self):
        return len(self.queue)
    
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        pq = customerPQ()
        visit = defaultdict(int)
        pq.put([0,0,-1])
        # visit[0] = True
        sumi = 0
        while len(pq)>0:
            wt,node,parent = pq.get()
            
            if visit[node]==True:
                continue
            
            visit[node] = True
            sumi+=wt
            
            for child in adj[node]:
                childNode,childWt = child
                if visit.get(childNode,False)==False:
                    # visit[childNode] = True
                    pq.put([childWt,childNode,node])
        
        return sumi
    
    
adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
v = 3
obj = Solution().spanningTree(v,adj)
print(obj)