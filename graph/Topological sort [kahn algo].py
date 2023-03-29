from collections import defaultdict, deque


def adjecentlist(edges):

    adj_list = defaultdict(list)
    num = len(edges)

    for ind in range(num):
        for data in edges[ind]:
            adj_list[data].append(ind)
    return adj_list


def toposort_kahn(adj):

    indegree = defaultdict(int)
    queue = deque()

    for ind, data in enumerate(adj):
        num = len(data)
        indegree[ind] = num
        if num == 0:
            queue.append(ind)

    ans = []
    adj = adjecentlist(adj)
    while queue:
        front = queue.popleft()
        ans.append(front)
        for data in adj[front]:
            indegree[data] -= 1
            if indegree[data] <= 0:
                queue.append(data)

    return ans


arr = [[], [0], [0], [0]]
print(toposort_kahn(arr))
