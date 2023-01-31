"""
URL : https://leetcode.com/problems/data-stream-as-disjoint-intervals/
"""
from typing import *


def checkingIndex(arr, low, high, k):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] > k:
            high = mid-1
        else:
            low = mid+1

    return low


class SummaryRanges:

    def __init__(self):
        self.start = {}

    def addNum(self, value: int) -> None:
        self.start[value] = True

    def getIntervals(self):
        res = []
        listing = sorted(self.start)
        for n in listing:
            if res and res[-1][1]+1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])

        return res


arr = [1, 2, 3, 4]

dist = {1: True, 0: False, 6: "A", 8: 6}
print(sorted(dist))
