"""
! URL : https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
"""

from queue import PriorityQueue
from collections import defaultdict


def minimumSPT(edges,v):
    def spanningTree( v, adj):
        # return adj
        pq = PriorityQueue()
        visit = defaultdict(bool)
        pq.put((0,0))
        
        sumi = 0
        while pq.empty()==False:
            weight,node = pq.get()
            if visit.get(node)==True:
                continue
            
            visit[node] = True
            sumi+=weight
            
            for edges in adj[node]:
                node,weight = edges
                if visit[node]==False:
                    pq.put((weight,node))
        return sumi
    
    return spanningTree(v,edges)