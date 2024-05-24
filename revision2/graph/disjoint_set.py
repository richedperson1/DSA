

class disJointSet:
    def __init__(self,v):
        self.rank = [0]*(v+1)
        self.parent = [ind for ind in range(v+1)]
        self.size = [1]*(v+1)
        
    def find_parent(self,node):
        if node==self.parent[node]:
            return node
        node_parent = self.find_parent(self.parent[node])
        self.parent[node] = node_parent
        return node_parent
    
    def parent_find(self,node):
        if node==self.parent[node]:
            return node
        
        # node_parent = self.find_parent(self.parent[node])
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self,u,v):
        parent_u = self.find_parent(u)
        parent_v = self.find_parent(v)
        if parent_u==parent_v:
            return "same"

        elif self.rank[parent_u]>self.rank[parent_v]:
            self.parent[parent_v] = parent_u
            
        elif self.rank[parent_v]>self.rank[parent_u]:
            self.parent[parent_u] = parent_v
        
        else:
            self.parent[parent_u] = parent_v 
            self.rank[parent_v]+=1
    
    def unionBySize(self,ultParentU,ultParentV):
        # ultParentU = self.parent_find(u)
        # ultParentV = self.parent_find(v)
        
        # if ultParentU==ultParentV:
        #     return
        if self.size[ultParentU]>self.size[ultParentV]:
            self.size[ultParentU] += self.size[ultParentV]
            self.parent[ultParentV] = ultParentU
            
        else:
            self.parent[ultParentU] = ultParentV
            self.size[ultParentV] += self.size[ultParentU]
            
            
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        
        pq = []
        for ind in range(V):
            for data in adj[ind]:
                v,w = data
                u = ind
                pq.append((w,u,v))
                pq.append((w,v,u))
    
            
        total = 0
        pq = sorted(pq)
        
        disjoint = disJointSet(V)
        
        visit = {}
        total = 0
        for data in pq:
            weight,start,end = data
            
            ultS = disjoint.find_parent(start)
            ultE = disjoint.find_parent(end)
            # print(data)
            if ultS!=ultE:
                total+= weight
                disjoint.unionBySize(ultS,ultE)
                
            print(data," parent ========> ",disjoint.parent," size ====> ", disjoint.size)
                
        return total
    
obj = Solution()

arr = [[[1, 3]], [[0, 3], [3, 3], [5, 10]], [[4, 6], [6, 9]], [[1, 3], [6, 8]], [[2, 6], [5, 6]], [[1, 10], [4, 6]], [[2, 9], [3, 8]]]
v = 7
print(obj.spanningTree(v,arr))