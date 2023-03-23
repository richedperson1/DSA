"""
URL: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


from collections import deque
from collections import defaultdict
arr = [[0, 1], [0, 2], [1, 2]]


def adjecent(adj, edges):
    n = len(edges)
    for num in range(n):
        u = edges[num][0]
        v = edges[num][1]
        adj[u].append(v)
        adj[v].append(u)

    return adj


def dfs_helper(node, adj, visited):
    visited[node] = True
    for child in adj[node]:
        if not(visited[child]):
            dfs_helper(child, adj, visited)


def dfs(vertix, n):
    adj_list = defaultdict(list)
    adj_list = adjecent(adj_list, vertix)
    visited = defaultdict(bool)

    total = -1
    for node in range(n):
        if not(visited[node]):
            dfs_helper(node, adj_list, visited)
            total += 1

    return total


print(dfs(arr, 4))
