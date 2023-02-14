

def adjecent(adj, edges):
    n = len(edges)
    for num in range(n):
        u = edges[num][0]
        v = edges[num][1]
        adj[u].append(v)
        adj[v].append(u)

    return adj
