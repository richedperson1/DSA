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
        self.stack = []
        self.dist = {}

    def addNum(self, value: int) -> None:
        n = len(self.stack)
        if n == 0:
            self.stack.append(value)
            return

        if value in self.dist:
            return
        self.dist[value] = 1
        ind = checkingIndex(self.stack, 0, n-1, value)
        self.stack.insert(ind, value)
        return

    def getIntervals(self):

        pass


arr = [1, 2, 3, 4]
# print(checkingIndex(arr, 0, 3, 8.5)).
