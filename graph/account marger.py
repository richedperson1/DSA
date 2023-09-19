from collections import defaultdict
class disJoint:
    def __init__(self,v):
        self.parent = [ind for ind in range(v)]
        self.rank   = [0]*v
    
    def findParent(self,u):
        if self.parent[u]==u:
            return u
            
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
        
    def unionByRank(self,u,v):
        ultU = self.findParent(u)
        ultV = self.findParent(v)
        
        if ultU==ultV:
            return
        
        if self.rank[ultV]>self.rank[ultU]:
            self.parent[ultU] = ultV
            
        elif self.rank[ultU]>self.rank[ultV]:
            self.parent[ultV] = ultU
            
        else:
            self.parent[ultU] = ultV
            self.rank[ultV] +=1
            
    
class Solution:
    def accountsMerge(self, accounts):
        # Code here
        size = len(accounts)
        
        mail2Node = defaultdict(int)
        dis = disJoint(size)
        for index in range(size):
            for pos in range(1,len(accounts[index])):
                mail = accounts[index][pos]
                if mail not in mail2Node:
                    mail2Node[mail] = index
                else:
                    dis.unionByRank(index,mail2Node[mail])
                    
        
        finalDist = defaultdict(list)
        # return mail2Node,dis.parent
        for data,ind in mail2Node.items():
            ultParent = dis.findParent(ind)
            finalDist[ultParent].append(data)
            
        
        finalOut = []
        for ind,data in finalDist.items():
            if data==[]:
                continue
            
            sData = sorted(data)
            sData.insert(0,accounts[ind][0])
            finalOut.append(sData)
        return finalOut
            
accounts  =[["John","johnsmith@mail.com","john_newyork@mail.com"],
["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

sol = Solution()
print(sol.accountsMerge(accounts))