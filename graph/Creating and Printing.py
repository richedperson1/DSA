"""
URL : https://www.codingninjas.com/codestudio/problems/create-a-graph-and-print-it_1214551
"""


def adjecent(ans, u, v):
    if ans.get(u, 0) != 0:
        ans[u].append(v)
        ans[u] = sorted(ans[u])
    else:
        ans[u] = [v]

    if ans.get(v, 0) != 0:
        ans[v].append(u)
        ans[v] = sorted(ans[u])
    else:
        ans[v] = [u]

    return ans


def printAdjacency(n, m, edges):
    # Write your code here.
    ans = {}
    for i in range(m):
        u = edges[i][0]
        v = edges[i][1]
        ans = adjecent(ans, u, v)

    adj = [0]*n
    for i in range(n):
        adj[i] = [i]
        sizeJ = ans.get(i, [])
        for final in sizeJ:
            adj[i].append(final)

    return adj
