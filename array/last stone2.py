
import heapq
"""
URL : https://leetcode.com/problems/last-stone-weight-ii/
"""

from math import ceil

arr = [[2, 7, 4, 1, 8, 1]][0]


def lastStoneWeightII(stones: list[int]) -> int:
    sumi = sum(stones)
    target = ceil(sumi/2)

    def divideStone(ind, total):
        if total >= target or ind >= len(stones):
            return abs(2*total-sumi)

        if (ind, total) in dp:
            return dp[(ind, total)]

        final = min(divideStone(ind+1, total),
                    divideStone(ind+1, total+stones[ind]))
        dp[(ind, total)] = final
        return final

    dp = {}
    return divideStone(0, 0)
