"""
! URL : https://practice.geeksforgeeks.org/problems/eventual-safe-states/1
"""
from collections import defaultdict

adj = [[1, 2], [2, 3], [5], [0], [5], [], []]
v = 7

def checkingCycle(adj,v):

    def dfs(node):
        visit[node] = True
        path[node] = 1

        childs = adj[node]
        for child in childs:
            if visit[child]==False:
                ans = dfs(child)
                if ans==True:
                    return True
                
            elif path[child]:
                return True
            
        path[node] =0
        safe[node] = 1
        return False
        
    visit = defaultdict(bool)
    path = [0]*(v+1)
    safe = [0]*(v+1)

    for vtx in range(v):
        if visit[vtx]==False:
            dfs(vtx)

    ans = []
    for ind,data in enumerate(safe):
        if data:
            ans.append(ind)

    return ans

print(checkingCycle(adj,v))