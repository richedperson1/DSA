class Solution:
    def Solve(self, n, adj):
        edge = len(adj)
        vert = n
        
        adjt = [[] for _ in range(edge)]
        for data in adj:
            start,end = data
            adjt[start].append(end)
            adjt[end].append(start)
            
        if vert-edge>1:
            return -1
            
        visit = {}
        stack = {}
        def dfs(node):
            
            for child in adjt[node]:
                if visit.get(child,False)==False:
                    visit[child] = True
                    dfs(child)
                
        
        total = 0
        for vtx in range(n):
            if visit.get(vtx,False)==False:
                total+=1
                dfs(vtx)
        
        return total-1
    

adj = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 3]]
adj = [[0,2],[0,2],[2,7],[7,9],[7,4],[7,9],[9,8],[8,5],[5,6],[3,1]]
n = len(adj)-1

obj = Solution()
print(obj.Solve(n,adj))