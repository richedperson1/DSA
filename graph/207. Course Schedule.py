"""
URL : https://leetcode.com/problems/course-schedule
"""

from collections import defaultdict


def adjecent_list(edges):
    n = len(edges)
    adj = defaultdict(list)
    for num in range(n):
        u = edges[num][0]
        v = edges[num][1]
        adj[v].append(u)

    return adj


def helper(node, adj, visit, dfs_visit):
    visit[node] = True
    dfs_visit[node] = True
    childNode = adj[node]
    for child in childNode:
        if not(visit[child]):
            if helper(child, adj, visit, dfs_visit):
                return True
        elif dfs_visit[child]:
            return True

    dfs_visit[node] = False
    return False


def isCyclic(V, adj):
    visit = defaultdict(bool)
    dfs_visit = defaultdict(bool)
    for ind in range(V):
        if not(visit[ind]) and helper(ind, adj, visit, dfs_visit):
            return True
    return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list = adjecent_list(prerequisites)
        visited = defaultdict(bool)
        dfs_visit = defaultdict(bool)
        for node in range(numCourses):
            if not(visited[node]) and helper(node, adj_list, visited, dfs_visit):
                return False
        return True
