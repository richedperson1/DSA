from collections import defaultdict


def adjecent_list(edges):
    adjList = defaultdict(list)
    indegree = defaultdict(int)
    for u, v in edges:
        adjList[u].append(v)
        indegree[v] += 1
    return adjList, indegree


def adjecent_list2(edges):
    adjList = defaultdict(list)
    indegree = defaultdict(int)
    for u, v in edges:
        adjList[v].append(u)
        indegree[u] += 1
    return adjList, indegree


def topoSort(edges, v):
    adjList, indegree = adjecent_list2(edges)

    res = []
    
    for data in range(v):
        if indegree[data] == 0:
            res.append(data)
            

    ans = []
    cnt = 0
    while res:
        front = res.pop()
        cnt+=1
        ans.append(front)
        for child in adjList[front]:
            if indegree[child] > 0:
                indegree[child] -= 1

            if indegree[child] == 0:
                res.append(child)

    return cnt,v


    ans = []
    adj = adjecentlist(adj)
    cnt = 0
    while queue:
        front = queue.popleft()
        cnt+=1
        ans.append(front)
        for data in adj[front]:
            indegree[data] -= 1
            if indegree[data] <= 0:
                queue.append(data)

    return cnt

edges = [[ 0,1], [2, 0], [3, 1], [3, 2]]
v = 4
# edges = []
# v = 1
print(topoSort(edges, v))
