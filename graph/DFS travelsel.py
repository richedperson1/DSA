from typing import *
from collections import *
# from math import *


def findAdj(edges, dist):
    n = len(edges[0])
    for ind in range(n):
        u = edges[0][ind]
        v = edges[1][ind]
        dist[u].append(v)
        dist[v].append(u)

    return dist


def dfs(n, visited, adj, ans):
    visited[n] = True
    ans.append(n)
    for num in adj[n]:
        if visited.get(num, 0) == 0:
            dfs(num, visited, adj, ans)


def depthFirstSearch(V, E, edges):
    # write your code here
    final = defaultdict(list)
    dist = findAdj(edges, final)
    final = []
    visited = {}

    for i in range(V):
        if visited.get(i, 0) == 0:
            ans = []
            dfs(i, visited, dist, ans)
            final.append(ans)
    return final


string = """
9 10
0 8
1 6
1 7
1 8
5 8
6 0
7 3
7 4
8 7
2 5
"""

edge = [[], []]
vertix = 4
for ind, num in enumerate(string.split("\n")):

    if ind == 1:
        spliting = list(map(int, num.split()))
        # print(spliting)
        vertix = spliting[0]
    if num == "":
        continue
    number = list(map(int, num.split()))
    edge[0].append(number[0])
    edge[1].append(number[1])

print(depthFirstSearch(vertix, 4, edge))
