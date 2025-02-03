

from collections import deque
def solve(n, edges, queries):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    ans = []
    for x, k in queries:
        # BFS to establish parent relationships
        parent = [None] * (n + 1)
        parent[x] = -1  # Root's parent is marked as -1
        q = deque([x])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parent[v] is None and v != parent[u]:
                    parent[v] = u
                    q.append(v)
        children = [[] for _ in range(n + 1)]
        for v in range(1, n + 1):
            if parent[v] != -1 and parent[v] is not None:
                children[parent[v]].append(v)
        
        sizes = [0] * (n + 1)
        stack = [(x, False)]
        while stack:
            node, processed = stack.pop()
            if processed:
                total = 1
                for child in children[node]:
                    total += sizes[child]
                sizes[node] = total
            else:
                stack.append((node, True))
                for child in reversed(children[node]):
                    stack.append((child, False))
        subtree_sizes = [sizes[i] for i in range(1, n + 1)]
        subtree_sizes.sort()
        ans.append(subtree_sizes[k - 1])
    return ans

# Example usage:
n = 3
edges = [[2, 1], [2, 3]]
queries = [[1, 2], [2, 2], [3, 2]]
n = 4
edges = [[2, 1], [3, 2], [1, 4]]
queries = [[1, 2], [1, 3], [1, 4]]
n = 5
edges = [[1, 2], [2, 3], [3, 4], [4, 5]]
queries = [[1, 3], [2, 2], [3, 1]]

n = 5
edges = [[1, 2], [1, 3], [1, 4], [1, 5]]
queries = [[1, 2], [2, 1], [3, 1]]



n = 3
edges = [[2, 1], [ 2,3]]
queries = [[1, 2], [2,2], [3, 2]]

n = 4
edges = [[2, 1], [3, 2], [1, 4]]
queries = [[1, 2], [1, 3], [1, 4]]

n = 1
edges = []
queries = [[1, 1]]
n = 5
edges = [[1, 2], [2, 3], [3, 4], [4, 5]]
queries = [[1, 3], [2, 2], [3, 1]]

n = 5
edges = [[1, 2], [1, 3], [1, 4], [1, 5]]
queries = [[1, 2], [2, 1], [3, 1]]


n = 4
edges = [[2, 1], [3, 2], [1, 4]]
queries = [[4, 2]]
# ================================================
n = 2
edges = [[1, 2]]
queries = [[1, 1], [2, 1]]
# Output: [1, 1]

n = 1
edges = []
queries = [[1, 1]]

n = 3
edges = [[1, 2], [2, 3]]
queries = [[1, 3], [3, 2]]
# Output: [3, 2]

n = 5
edges = [[1, 2], [1, 3], [1, 4], [1, 5]]
queries = [[1, 1], [1, 4], [1, 5]]
# Output: [1, 1, 5]


n = 7
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
queries = [[1, 5], [1, 6], [1, 7]]
# Output: [3, 3, 7]

print(solve(n, edges, queries))  # Output: [2, 1, 2]


arr = [[2, 3], [3, 4], [5, 5], [3, 4]]
queries = [[1, 2], [3, 4]]
