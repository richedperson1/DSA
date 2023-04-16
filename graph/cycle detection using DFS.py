from collections import defaultdict

from collections import deque


def adjecent(adj, edges):
    n = len(edges)
    for num in range(n):
        u = edges[num][0]
        v = edges[num][1]
        adj[u].append(v)
        adj[v].append(u)

    return adj


def cyclePreset(node, parent, visited, adj):
    visited[node] = True
    for child in adj[node]:
        if visited[child] == False:
            if cyclePreset(child, node, visited, adj):
                return True

        elif child != parent:
            return True
    return False


def cycle(edge, v):
    adj = defaultdict(list)
    adj = adjecent(adj, edge)
    visited = defaultdict(bool)
    for ind in range(v):
        if visited[ind] == False:
            if cyclePreset(ind, -1, visited, adj):
                return True

    return False


v = 2
edge = [[0, 1], [1, 0]]
print(cycle(edge, v))
