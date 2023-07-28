from collections import defaultdict


def adjecentlist(edges):

    adj_list = defaultdict(list)
    num = len(edges)

    for ind in range(num):
        u = edges[ind][0]
        v = edges[ind][1]

        adj_list[u].append(v)
        # adj_list[v].append(u)

    return adj_list





def helper(node, visited, adj, final):
    visited[node] = True
    childNode = adj[node]

    for child in childNode:
        if not(visited[child]):
            helper(child, visited, adj, final)

    final.append(node)


def cycle_Detect(adjenet, vertex):
    visited = defaultdict(bool)
    adj_list = adjecentlist(adjenet)
    final = []
    for node in range(1, 1+vertex):
        if not(visited[node]):
            helper(node, visited, adj_list, final)

    return final[::-1]


arr = [[1, 2], [1, 3], [2, 3]]

print(cycle_Detect(arr, 3))
