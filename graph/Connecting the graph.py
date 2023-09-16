class disJointSet:
    def __init__(self,n) -> None:
        self.rank = [0]*(n)
        self.parent = [i for i in range(n)]
        self.countIngSame = 0  

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
            self.countIngSame+=1
            return "Same"
        
        if self.rank[ultParU]<self.rank[ultParV]:
            self.parent[ultParU] = ultParV
        elif self.rank[ultParU]>self.rank[ultParV]:
            self.parent[ultParV] = ultParU
        else:

            self.parent[ultParV] = ultParU
            self.rank[ultParU]+=1


def numProvinces( adj, v):
    
    dis = disJointSet(v)
    for row,col in adj:
        dis.unionByRank(row,col)
        
    count = -1
    for ind,data in enumerate(dis.parent):
        if ind==data:
            count+=1
    
    # return dis.parent
    if count>dis.countIngSame:
        return -1
    
    return count


adj = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
v = 6

print(numProvinces(adj,v))