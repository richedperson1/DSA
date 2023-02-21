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


def isCycle(adj, visited, ind):
    parent = defaultdict(int)
    parent[ind] = -1
    visited[ind] = True
    que = deque([ind])
    while que:
        front = que.popleft()
        for neigh in adj[front]:
            if visited[neigh] and neigh != parent[front]:
                return True
            elif not(visited[neigh]):
                que.append(neigh)
                visited[neigh] = True
                parent[neigh] = front
    return False


def cycleDetection(edges, n, m):
    listing = defaultdict(list)
    listing = adjecent(listing, edges)

    visited = defaultdict(bool)
    for ind in range(1, n+1):
        if visited.get(ind, 0) == 0:
            ans = isCycle(listing, visited, ind)
            if ans:
                return "Yes"
    return "No"
