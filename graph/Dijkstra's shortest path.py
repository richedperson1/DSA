from heapq import heapify, heappush, heappop
from collections import defaultdict


class nodeClass:
    def __init__(self, w, n) -> None:
        self.weight = w
        self.node = n

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __repr__(self) -> str:
        return str(str(self.weight)+" = " + str(self.node))


def dijstra_algo(edges, vert, src):
    num = len(edges)
    dist = [float("inf")]*vert
    dist[src] = 0

    ans = [nodeClass(0, 0)]
    # visited = defaultdict(bool)
    while ans:
        top_list = heappop(ans)
        childs = edges[top_list.node]

        for child in childs:
            node = child[0]
            weight2 = abs(dist[node])
            weight = abs(top_list.weight)
            total_w = abs(weight)+abs(child[-1])

            if total_w < weight2:
                first_record = nodeClass(-dist[child[0]], child[0])
                if first_record in ans:
                    print(first_record)
                    ans.remove(first_record)
                    heapify(ans)
                heappush(ans, nodeClass(-total_w, node))
                dist[node] = total_w

    return dist

def shortPath2(edges,n):
    adj = [[] for ind in range(n+1)]
    for data in edges:
        u,v,w = data
        adj[u].append([v,w])
        adj[v].append([u,w])
    
        
    dist = [float("inf")]*(n+1)
    dist[1] = 0
    def dfs(node):
        for child in adj[node]:
            childNode,childWeight = child
            localWeight = dist[node]+childWeight
            if localWeight < dist[childNode]:
                dist[childNode] = localWeight
                dfs(childNode)

    dfs(1)
    return dist[1:]

V = 3
E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]

answer = dijstra_algo(adj, V, 0)
print(answer)
# actual = [nodeClass(5, 2)]
# heapify(actual)
# heappush(actual, nodeClass(7, 5))

# print(heappop(actual))

n = 5 
m= 6
edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
print(shortPath2(edges,n))