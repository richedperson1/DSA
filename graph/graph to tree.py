from typing import (
    List,
)
from collections import defaultdict


def adjecent(edges):
    listing = defaultdict(list)

    for edge in edges:
        u = edge[0]
        v = edge[1]
        listing[u].append(v)
        listing[v].append(u)
    return listing


def dfsCall(node, parent, visited, adjList):
    visited[node] = True

    childs = adjList[node]
    for child in childs:
        if visited.get(child, False) == False:
            if dfsCall(child, node, visited, adjList):
                return True

        elif parent != child:
            return True
    return False


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        # if len(edges) <= 1:
        #     return True
        adjList = adjecent(edges)

        visited = defaultdict(bool)
        i = 0
        for ind in range(n):
            # print(visited.get(ind))
            if visited.get(ind, False) == False:
                i += 1
                if dfsCall(ind, -1, visited, adjList):
                    return False

            if i > 1:
                return False

        return True
