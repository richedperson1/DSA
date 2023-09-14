
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


dis = disJointSet(7)
dis.unionByRank(1,2)        
dis.unionByRank(2,3)        
dis.unionByRank(4,5)
dis.unionByRank(2,5)

print(dis.findParent(4),dis.findParent(5),dis.parent)
