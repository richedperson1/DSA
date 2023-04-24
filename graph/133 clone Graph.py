# Definition for a Node.
from collections import *


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(root: 'Node') -> 'Node':
    allStack = defaultdict(list)
    queue = deque([root])
    visited = defaultdict(bool)

    while queue:
        ele = queue.popleft()
        val = ele.val
        visited[ele] = True
        allStack[ele] = Node(val)

        for child in ele.neighbors:
            if visited[child] == False and child:
                queue.append(child)

    rootClone = allStack[root]
    queue = deque([root])
    visited = defaultdict(bool)
    while queue:
        root1 = queue.popleft()
        root2 = allStack[root1]
        visited[root1] = True

        for child in root1.neighbors:
            if visited[child] == False:
                queue.append(child)
            root2.neighbors.append(allStack[child])

    return rootClone


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
num = len(adjList)
dist = {}
for ind in range(len(adjList)):
    dist[ind+1] = Node(ind+1)


for
