from collections import defaultdict,deque
adj = [[0,1,1],[0,2,3],[1,2,1],[2,3,3]]

adjList = [[(1,1),(2,3)],[(2,1)],[(3,3)],[],[]]
n = 5

def adjlist1(adj,n):
    adjlisting = [[]  for ind in range(n)]
    for data in adj:
        u,v,w = data
        adjlisting[u].append((v,w))
    return adjlisting

def shortestDistance(adjList,n):

    queue = deque([0])
    ans = [float("inf")]*(n)
    ans[0] = 0
    while queue:
        node = queue.popleft()

        for child in adjList[node]:
            local = ans[node]+child[-1]
            if local>ans[child[0]]:
                continue
            else:
                ans[child[0]] = min(local,ans[child[0]])
                queue.append(child[0])
    
    for ind,data in enumerate(ans):
        if data >=float('inf'):
            ans[ind] = -1
    return ans
            
print(shortestDistance(adjList,n))
