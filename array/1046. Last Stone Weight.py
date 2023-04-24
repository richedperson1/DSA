"""
URL : https://leetcode.com/problems/last-stone-weight/
"""
import heapq


arr = [2]


for ind, data in enumerate(arr):
    arr[ind] = -data


heapq.heapify(arr)

while len(arr) > 1:
    first = heapq.heappop(arr)
    second = heapq.heappop(arr)
    if first != second:
        heapq.heappush(arr, abs(first-second))
