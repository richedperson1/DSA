"""
URL : https://leetcode.com/problems/reducing-dishes/
"""
import sys
arr = [-1, -8, 0, 5, -9]

arr = sorted(arr)


def maxiMumSati(arr, time, ind, n):
    if ind >= n:
        return 0

    inc = maxiMumSati(arr, time+1, ind+1, n)+arr[ind]*time

    exc = maxiMumSati(arr, time, ind+1, n)

    return max(inc, exc)


def maximumSatDP(arr, time, ind, n, dp):
    if ind >= n:
        return 0

    if dp[ind][time] != -1:
        return dp[ind][time]
    inc = maximumSatDP(arr, time+1, ind+1, n, dp)+arr[ind]*time

    exc = maximumSatDP(arr, time, ind+1, n, dp)

    ans = max(inc, exc)
    dp[ind][time] = ans
    return ans


def maxiMumSatTab(arr):
    time = 1
    n = len(arr)
    dp = [[0]*(n+1) for i in range(n+1)]

    for i in range(n-1, -1, -1):
        for time in range(i, -1, -1):
            inc = arr[i]*(time+1) + dp[i+1][time+1]
            exc = dp[i+1][time+1]
            ans = max(inc, exc)
            dp[i][time] = ans
    return dp


def maximumSatTabObtimize(arr):
    n = len(arr)
    curr = [0]*(n+1)
    next = [0]*(n+1)
    for ind in range(n-1, -1, -1):
        for time in range(ind, -1, -1):
            inc = next[time+1]+arr[ind]*time
            exc = next[time+1]
            curr[time] = max(inc, exc)

        next = curr

    return next[0]


arr = [-1, -8, 0, 5, -9]
arr = [4, 3, 2]

arr = sorted(arr)
time = 1
n = len(arr)
ans = maxiMumSati(arr, time, 0, n)

dp = [[-1]*(n+1) for i in range(n+1)]
time = 1
n = len(arr)
print(maximumSatDP(arr, time, 0, n, dp))
print(maxiMumSatTab(arr))
print(maximumSatTabObtimize(arr))
