"""
URL : https://leetcode.com/problems/min-cost-climbing-stairs/

"""
import sys

"""
Time complexity : O(2^n)
space complexity : O(n)
"""
# Method 1


def miniCost(arr, ind, total, prev):
    if ind < 0:
        return total

    if prev == True:
        c1 = miniCost(arr, ind-1, total+arr[ind], True)
        c2 = miniCost(arr, ind-1, total, False)
        return min(c1, c2)
    else:
        return miniCost(arr, ind-1, total+arr[ind], True)

# Method 2


def miniCost2(arr, ind, prev):
    # if ind == 0:
    #     return arr[ind]
    if ind >= len(arr):
        return 0

    if prev == True:
        c1 = miniCost2(arr, ind+1, True)+arr[ind]
        c2 = miniCost2(arr, ind+1,  False)
        return min(c1, c2)
    else:
        return miniCost2(arr, ind+1, True)+arr[ind]


def miniCostDP(arr, ind, prev, dp):
    # if ind == 0:
    #     return arr[ind]
    if ind >= len(arr):
        return 0

    if dp[ind] != -1:
        return dp[ind]

    if prev == True:
        c1 = miniCostDP(arr, ind+1, True, dp)+arr[ind]
        c2 = miniCostDP(arr, ind+1,  False, dp)
        dp[ind] = min(c1, c2)
        return min(c1, c2)
    else:
        dp[ind] = miniCostDP(arr, ind+1, True, dp)+arr[ind]
        return dp[ind]


arr = [10, 15, 20]
arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]


print(miniCost2(arr, 0, True))
dp = [-1]*(len(arr)+1)
print(miniCostDP(arr, 0, True, dp))
