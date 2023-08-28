from collections import defaultdict
from queue import PriorityQueue

def CheapestFLight(n,flights,src,dst,k):
    if src==dst:
        return 0
    
    adj = defaultdict(list)
    
    for start,end,weight in flights:
        adj[start].append((end,weight))
    
        
    pq = PriorityQueue()
    pq.put((0,src,0))
    dist = defaultdict(lambda : float("inf"))
    dist[src] = 0
    while not pq.empty():
        step,node,nWeight = pq.get()
        
        for childNode,cWeight in adj[node]:
            localWeight = cWeight+nWeight
            if dist[childNode]> localWeight and step<=k:
                pq.put((step+1,childNode,localWeight))
                dist[childNode] = localWeight
            
    return dist[dst]
            
"""
5 6
0 1 5
0 3 2
1 4 1
1 2 5
4 2 1
3 1 2
0 
2 
2
"""
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 2

# flights = [[0, 1, 5], [0, 3, 2], [1, 4, 1], [1, 2, 5], [4, 2, 1], [3, 1, 2]]
# n = 5
# k = 2
# src =0
# dst = 2


# flights = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1], [3, 4, 1]]
# n = 5
# k = 2
# src =0
# dst = 4
print(CheapestFLight(n,flights,src,dst,k))