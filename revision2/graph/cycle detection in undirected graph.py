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


def helper2(node, visit, adj, dfs_visit):
    visit[node] = True
    dfs_visit[node] = True
    childNode = adj[node]

    for child in childNode:
        if not(visit[child]):
            if helper2(child, visit, adj, dfs_visit):
                return True
        elif dfs_visit[child]:
            return True

    dfs_visit[node] = False
    return False


def helper(node, visited, adj, dfs_visit):

    visited[node] = True
    dfs_visit[node] = True

    for child in adj[node]:
        if not(visited[child]):
            ans = helper(child, visited, adj, dfs_visit)
            if ans:
                return True

        elif dfs_visit[child]:
            return True

    dfs_visit[node] = False

    return False


def cycle_Detect(adjenet, vertex):
    visited = defaultdict(bool)
    adj_list = adjecentlist(adjenet)
    dfs_call = defaultdict(bool)
    final = []
    for node in range(1, 1+vertex):
        if not(visited[node]):
            ans = helper(node, visited, adj_list, dfs_call)
            if ans:
                return ans

    return False


arr = [[1, 2], [1, 3], [2, 3]]

# listing = adjecentlist(arr)

print(cycle_Detect(arr, 4))


def isCycle( V: int, adj: list[list[int]]) -> bool:
    #Code here
    visit = set()
    def dfs(src,parent):
        visit.add(src)
        
        for childNode in adj[src]:
            if childNode not in visit:
                ans = dfs(childNode,src)
                if ans:
                    return True
            
            elif childNode !=parent:
                return True

                    
        return False
    
    for vert in range(V):
        if vert not in visit:
            if dfs(vert,-1):
                return True
    return False

