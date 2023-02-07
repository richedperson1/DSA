"""
URL : https://leetcode.com/problems/fruit-into-baskets/description/
"""
from collections import *


def fruitsBucket(arr):

    ans = 0
    dist = defaultdict(int)
    l = 0
    for ind, data in enumerate(arr):
        dist[data] += 1
        while len(dist) > 2:
            dist[arr[l]] -= 1
            if dist[arr[l]] == 0:
                del dist[arr[l]]
            l += 1

        ans = max(ans, ind-l+1)


arr = [3, 3, 3, 1, 3, 2, 2, 1, 1, 2, 3, 3, 4]


print((fruitsBucket(arr)))
