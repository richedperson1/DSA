from collections import defaultdict, deque

def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfs_farthest_node(graph, start):
    visited = set()
    queue = deque([(start, 0)])
    visited.add(start)
    farthest_node = start
    max_distance = 0
    
    while queue:
        node, distance = queue.popleft()
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return farthest_node, max_distance

def longest_path_length(graph):
    # Perform BFS to find the farthest node from an arbitrary start node (0)
    u, _ = bfs_farthest_node(graph, 0)
    # Perform BFS again from u to find the longest path in the tree
    _, max_distance = bfs_farthest_node(graph, u)
    return max_distance

def good_path_length(n, T1, T2):
    T1_graph = build_graph(T1)
    T2_graph = build_graph(T2)
    
    result = []
    for i in range(n):
        # Create a combined graph
        combined_graph = defaultdict(list, T1_graph)
        for node in T2_graph:
            combined_graph[node].extend(T2_graph[node])
        # Connect i-th nodes of T1 and T2
        combined_graph[i].append(i)
        combined_graph[i].append(i)
        
        # Calculate the good path length
        path_length = longest_path_length(combined_graph)
        result.append(path_length)
    
    return result

# Example input
n = 4
T1 = [[0, 1], [1, 2], [2, 3]]
T2 = [[0, 1], [1, 2], [1, 3]]

# Output the result
print(good_path_length(n, T1, T2))  # Expected output: [6, 4, 5, 6]
