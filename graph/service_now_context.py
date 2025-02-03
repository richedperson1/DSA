from collections import defaultdict
def compute_subtree_sizes(n, edges):

    # Build the adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Initialize subtree sizes and visited array
    subtree_size = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        size = 1  # Count the node itself
        for neighbor in tree[node]:
            if not visited[neighbor]:
                size += dfs(neighbor)
        subtree_size[node] = size
        return size

    # Perform DFS from an arbitrary root, e.g., node 1
    dfs(1)

    return subtree_size

def process_queries(subtree_size, queries):
    # Extract all subtree sizes (excluding the 0th index)
    sizes = subtree_size[1:]
    # Sort the sizes in non-decreasing order
    sorted_sizes = sorted(sizes)
    results = []
    for x, k in queries:
        # Since the sizes are precomputed and sorted, we can directly access the k-th smallest
        if 1 <= k <= len(sorted_sizes):
            results.append(sorted_sizes[k - 1])
        else:
            # If k is out of bounds, handle accordingly (e.g., return None or an error)
            results.append(None)
    return results
# ==========================================================================

def compute_subtree_sizes(tree, root, n):
    subtree_size = [0] * (n + 1)
    visited = [False] * (n + 1)

    def dfs(node):
        visited[node] = True
        size = 1  # Count the node itself
        for neighbor in tree[node]:
            if not visited[neighbor]:
                size += dfs(neighbor)
        subtree_size[node] = size
        return size
    dfs(root)
    return subtree_size

def process_queries(n, edges, queries):
    from collections import defaultdict

    # Build the adjacency list
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    results = []
    for x, k in queries:
        subtree_size = compute_subtree_sizes(tree, x, n)
        sizes = subtree_size[1:]
        sorted_sizes = sorted(sizes)
        if 1 <= k <= len(sorted_sizes):
            results.append(sorted_sizes[k - 1])
        else:
            results.append(None)
    return results





# =================================
# Example usage:

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

n = 7
edges = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
queries = [[1, 5], [1, 6], [1, 7]]
# Output: [3, 3, 7]

n = 2
edges = [[1, 2]]
queries = [[1, 1], [2, 1]]
# Output: [1, 1]

n = 5
edges = [[1, 2], [1, 3], [1, 4], [1, 5]]
queries = [[1, 1], [1, 4], [1, 5]]
# Output: [1, 1, 5]

n = 3
edges = [[1, 2], [2, 3]]
queries = [[1, 3], [3, 2]]
# Output: [3, 2]

n = 1
edges = []
queries = [[1, 1]]
# Output: [1]


results = process_queries(n, edges, queries)
print(results)  # Output: [1, 2, 4]


# subtree_size = compute_subtree_sizes(n, edges)
# results = process_queries(subtree_size, queries)
# print(results)  # Output: [1, 2, 4]
