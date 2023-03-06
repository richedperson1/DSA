"""
URL : https://leetcode.com/problems/jump-game-iv/
"""
from collections import defaultdict
from sortedcontainers import SortedSet
import sys
sys.setrecursionlimit(10000)
arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]


dist = defaultdict(list)

for ind, data in enumerate(arr):
    dist[data].append(ind)


def helper(adj, node, visit):
    visit[node] = True
    nodes = adj[node]

    ans = 0
    for noe in nodes:
        if not(visit[noe]):
            if noe == len(arr)-1:
                return 1
            return helper(adj, noe, visit)+1

    return ans


def jumpGame4(arr, adjecent, ind, visit):

    final = sys.maxsize
    for ind in range(len(arr)):
        if not(visit[ind]):
            local = helper(adjecent, ind, visit)
            final = min(local, final)

    return final


n = len(arr)
dp = [-1]*n
visit = defaultdict(bool)
print(jumpGame4(arr, dist, 0, visit))
