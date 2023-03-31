from collections import defaultdict
n = 6
m = 7
edge = [[0, 1, 2], [0, 4, 1], [4, 5, 4], [
    4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]

edge = [[0, 1, 5], [0, 2, 3], [1, 2, 2], [1, 3, 6], [
    2, 3, 7], [2, 4, 4], [2, 5, 2], [3, 4, -1], [4, 5, -2]]


def adjecent_list(edge):
    adj = defaultdict(list)
    num = len(edge)

    for ind in range(num):
        u = edge[ind][0]
        v = edge[ind][1]
        w = edge[ind][2]
        adj[u].append([v, w])

    return adj


def topoHelper(node, adjecent, visited, final):
    visited[node] = True
    childs = adjecent[node]
    for child in childs:
        child = child[0]
        if not(visited[child]):
            topoHelper(child, adjecent, visited, final)

    final.append(node)


def toposort(edges, n):
    adjecent = adjecent_list(edges)
    visited = defaultdict(bool)

    final = []
    for ind in range(n):
        if not(visited[ind]):
            topoHelper(ind, adjecent, visited, final)

    dist = [float("inf")]*n

    dist[1] = 0

    while final:
        ind = final.pop()
        if dist[ind] != float("inf"):
            childs = adjecent[ind]
            for child in childs:
                w = child[-1]
                val = child[0]

                local = min(dist[ind]+w, dist[val])
                dist[val] = local
    return dist if not(all(dist)) else -1


print(toposort(edge, n))
