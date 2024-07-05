from queue import PriorityQueue
from collections import defaultdict

class disJointSet:
    def __init__(self,n) -> None:
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]


    def findParent(self,u):
        if self.parent[u]==u:
            return u
        
        ultParentU = self.findParent(self.parent[u])
        self.parent[u] = ultParentU
        return ultParentU
    
    def unionByRank(self,u,v):
        ultParU = self.findParent(u)
        ultParV = self.findParent(v)
        if ultParU==ultParV:
            return "Same"
        
        if self.rank[ultParU]<self.rank[ultParV]:
            self.parent[ultParU] = ultParV
        elif self.rank[ultParU]>self.rank[ultParV]:
            self.parent[ultParV] = ultParU
        else:

            self.parent[ultParV] = ultParU
            self.rank[ultParU]+=1


def mstUsingMST(vi,adj):
    pq = []

    for ind in range(vi):
        for data in adj[ind]:
            v,w = data
            u = ind
            pq.append((w,u,v))

    dis = disJointSet(vi)
    total = 0
    while pq:
        w,u,v = pq.pop(0)
        
        ultU = dis.findParent(u)
        ultV = dis.findParent(v)
        
        if ultU!=ultV:
            total+=w
            dis.unionByRank(u,v)
    return total



adj = [[[1, 5], [2, 1]], [[0, 5], [2, 3]], [[1, 3], [0, 1]]]
v = len(adj)
print(sorted(adj))
print(sorted(mstUsingMST(v,adj)))