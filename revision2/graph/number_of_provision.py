#User function Template for python3
from collections import defaultdict
class disjoint:
    def __init__(self,v):
        self.parent = [ind for ind in range(v)]
        self.size = [1]*v
    
    def find_parent(self,root):
        if self.parent[root]==root:
            return root
        
        self.parent[root] = self.find_parent(self.parent[root])
        
        return self.parent[root]
        
    
    def union_by_size(self,rNode,lNode):
        ult_a = self.find_parent(rNode)
        ult_b = self.find_parent(lNode)
        if ult_a==ult_b:
            return
        
        if self.size[ult_a]>self.size[ult_b]:
            self.parent[ult_b] = ult_a
            self.size[ult_a]+= self.size[ult_b]
        else:
            self.parent[ult_a] = ult_b
            self.size[ult_b]+= self.size[ult_a]

class Solution:
    def numProvinces(self, adj, V):
        
        dis = disjoint(V)
        # adj = defaultdict(list)
        for ind,data in enumerate(adj):
            for to_ind , node in enumerate(data):
                if node==1:
                    dis.union_by_size(ind,to_ind)
                    # print(node,ind,to_ind)
                    # adj[ind].append(to_ind)
                    # adj[to_ind].append(ind)
        print(dis.parent)
        total = 0
        for ind,data in enumerate(dis.parent):
            if ind==data:
                total+=1
        return total
    

v = 4
arr = [
    [0,0,0,0],
    [0,1,0,1],
    [0,0,1,0],
    [0,1,0,1],
    ]


obj = Solution()

print(obj.numProvinces(arr,v))