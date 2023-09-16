from queue import PriorityQueue
from collections import defaultdict

class disJointSet:
    def __init__(self,n) -> None:
        self.rank = [0]*(n)
        self.parent = [i for i in range(n)]


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


def numProvinces( adj, v):
    # return adj
    dis = disJointSet(v)
    
    rows,cols = len(adj),len(adj[0])
    for row in range(rows):
        for col in range(cols):
            if row==col or adj[row][col]!=1:
                continue
            else:
                
                dis.unionByRank(row,col)
    return dis.parent
    return len(set(dis.parent))



adj = [
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]

# adj = [
#  [1, 1],
#  [1, 1]
# ]
v = len(adj)

print(numProvinces(adj,v))