#User function Template for python3
from collections import defaultdict
class disjoint:
    def __init__(self,v):
        self.parent = [_ for _ in range(v)]
        
        self.size = [1]*v
        
    def find_parent(self,node):
        if self.parent[node]==node:
            return node
        
        self.parent[node] = self.find_parent(self.parent[node])
        
        return self.parent[node]
    
    def unionBySize(self,start,end):
        ultS = self.find_parent(start)
        ultE = self.find_parent(end)
        
        if ultS==ultE:
            return
        
        elif self.size[ultS]>self.size[ultE]:
            self.parent[ultE] = ultS
            self.size[ultS] += self.size[ultE]
        
        else:
            self.parent[ultS] = ultE
            self.size[ultE] += self.size[ultS]
            
class Solution:
    def accountsMerge(self, accounts):
        
        size = len(accounts)
        dis = disjoint(size)
        
        mail2node = defaultdict(str)
        for index in range(size):
            for position in range(1,len(accounts[index])):
                mail = accounts[index][position]
                if mail2node.get(mail,-2)==-2:
                    mail2node[mail] = index
                else:
                    dis.unionBySize(index,mail2node[mail])
        
                parent = dis.parent
        print(dis.parent)
        final_out = defaultdict(list)
        
        for mail,val in mail2node.items():
            ultP = dis.find_parent(val)
            final_out[ultP].append(mail)
            
        result = []
        
        for key,data in final_out.items():
            if data==[]:
                continue
            
            data = sorted(data)
            data.insert(0,accounts[key][0])
            result.append(data)
        return result
    
n = 4
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

obj = Solution()
print(obj.accountsMerge(accounts))