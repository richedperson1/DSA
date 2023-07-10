from collections import defaultdict
def numProvinces( adj, V):

    def dfs(node):

        visit[node] = True
        listing = adj[node]
        
        for ind,data in enumerate(listing):
            if visit[ind]==False and data==1:
                dfs(ind)
                
    count = 0
    visit = defaultdict(bool)
    # visit[0] = True
    for node in range(V):
        if visit[node]==False :
            count+=1
            dfs(node)
            
    return count

adj = [
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]
]

v = len(adj)

print(numProvinces(adj,v))