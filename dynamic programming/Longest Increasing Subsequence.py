"""
URL : https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
"""
import sys


arr = [5, 8, 3, 7, 9, 1]

# arr = [5, 1, 6]


def longIncreasing(arr, ind, prev):
    n = len(arr)
    if ind >= n:
        return 0

    if prev < arr[ind]:
        inc = longIncreasing(arr, ind+1, arr[ind])+1
        exc = longIncreasing(arr, ind+1, prev)
        return max(inc, exc)
    else:
        exc = longIncreasing(arr, ind+1, prev)
        return exc


def longIncreasingDP(arr, ind, prev, dp):
    n = len(arr)
    if ind >= n:
        return 0

    if dp[ind][prev] != -2:
        return dp[ind][prev]

    inc = 0
    if prev == -1 or arr[prev] < arr[ind]:
        inc = longIncreasingDP(arr, ind+1, ind, dp)+1

    exc = longIncreasingDP(arr, ind+1, prev, dp)
    dp[ind][prev] = max(inc, exc)

    return dp[ind][prev]


print(longIncreasing(arr, 0, -1))
n = len(arr)
dp = [[-2]*(n+1) for i in range(n+1)]
# print(dp[5][4])
print(longIncreasingDP(arr, 0, -1, dp))
