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


def cycleDetect(edges, n):
    que = defaultdict(list)
    adj_list = adjecent(que, edges)
