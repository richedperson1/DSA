"""
? URL : https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1
"""

def shortPath2(edges,n):
    adj = [[] for ind in range(n+1)]
    for data in edges:
        u,v,w = data
        
        adj[u].append([v,w])
        adj[v].append([u,w])
    
        
    dist = [float("inf")]*(n+1)
    parent = [ind for ind in range(n+1)]
    dist[1] = 0
    parent[1] = -1
    def dfs(node):
        for child in adj[node]:
            childNode,childWeight = child
            localWeight = dist[node]+childWeight
            if localWeight < dist[childNode]:
                dist[childNode] = localWeight
                parent[childNode] = node
                dfs(childNode)

    dfs(1)
    ans = [5]
    ind = 5
    while dist[ind]!=1:
        ans.append(parent[ind])
        ind = parent[ind]

    ans.append(1)
    return parent


n = 5 
m= 6
edges = [[1,2,3], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
edges = [[1,2,3], [2,5,2], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
print(shortPath2(edges,n))