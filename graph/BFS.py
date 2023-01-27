from collections import *
# from math import *

# from collections import deque


def adjecent(ans, u, v):
    if ans.get(u, 0) != 0:

        local = sorted(ans[u] + [v])
        ans[u] = local

        # ans[u] = sorted(ans[u])
    else:
        ans[u] = [v]

    if ans.get(v, 0) != 0:
        local = sorted(ans[v] + [u])
        ans[v] = local

    else:
        ans[v] = [u]

    return ans


def findAdj(edges, dist):
    n = len(edges[0])
    for ind in range(n):
        u = edges[0][ind]
        v = edges[1][ind]
        dist = adjecent(dist, u, v)

    return dist


def dfs(visited, dist, ans, i):
    queue = deque([i])
    while queue:
        rootNode = queue.popleft()
        if visited.get(rootNode, False) == False:
            ans.append(rootNode)
        visited[rootNode] = True
        # ans.append(rootNode)
        for data in dist.get(rootNode, []):
            if visited.get(data, 0) == 0:
                queue.append(data)


def BFS(vertex, edges):

    dist = findAdj(edges, {})
    visited = {}
    ans = []
    for i in range(vertex):
        if visited.get(i, 0) != True:
            dfs(visited, dist, ans, i)

    print(dist)
    for i in range(vertex):
        if i not in ans:
            ans.append(i)
    return ans


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

print(edge)
print(BFS(vertix, edge))
