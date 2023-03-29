from collections import defaultdict, deque

arr = [[2, 3, 4], [1, 5], [1, 8], [1, 6], [2, 8], [4, 7], [6, 8], [3, 5, 7]]


def adjenect(edges, v):
    link = defaultdict(list)
    num = len(edges)

    for ind in range(v):
        first = arr[ind]
        link[ind+1] = first

    return link


def dfs(edges, v):
    visited = defaultdict(bool)
    parent = defaultdict(int)
    links = adjenect(edges, v)
    queue = deque([1])
    parent[1] = -1
    visited[1] = True
    while queue:

        front = queue.popleft()
        for child in links[front]:
            if not(visited[child]):
                parent[child] = front
                visited[child] = True
                queue.append(child)

    ans = []
    node = 8
    print(parent)
    while node >= 1:
        ans.append(node)
        node = parent[node]

    # ans.append(1)
    return ans[::-1]


print(dfs(arr, 8))
