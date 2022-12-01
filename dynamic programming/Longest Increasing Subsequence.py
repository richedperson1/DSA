"""
URL : https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
"""
import sys


"""
Time complexity : O(2^n)
Space complexity : O(n)
"""


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


"""
Time complexity : O(n^2)
Space complexity : O(n^2)

"""


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


"""
Time complexity : O(n^2)
Space complexity : O(n^2)

"""


def lengthOfLIS(arr: list[int]) -> int:
    n = len(arr)
    dp = [[0]*(n+1) for i in range(n+1)]
    for curr in range(n-1, -1, -1):
        for prev in range(curr-1, -2, -1):
            take = 0
            if prev == -1 or arr[curr] > arr[prev]:
                take = dp[curr+1][curr+1]+1

            notake = dp[curr+1][prev+1]
            dp[curr][prev+1] = max(take, notake)

    return dp[0][0]


"""
Time complexity : O(n^2)
Space complexity : O(n)

"""


def spaceOptimizeDP(arr):
    n = len(arr)
    if n <= 0:
        return 0
    dp = [1]*(n+1)
    for curr in range(n-1, -1, -1):
        for next in range(curr+1, n):
            if arr[curr] < arr[next]:
                dp[curr] = max(dp[curr], 1+dp[next])

    return max(dp)


def findInd(arr, k):
    low = 0
    high = len(arr)-1
    mid = 0
    while low < high:
        mid = (low+high)//2
        if arr[mid] < k:
            ans = mid
            low = mid+1
        else:
            high = mid-1
    return mid


def binarySearchLong(arr):
    if len(arr) < 1:
        return 0
    ans = [arr[0]]
    n = len(arr)
    for i in range(1, n):
        if ans[-1] < arr[i]:
            ans.append(arr[i])
        else:
            ind = findInd(ans, arr[i])
            ans[ind] = arr[i]

    return len(ans)


arr = [10, 9, 2, 5, 3, 7, 101, 18]
arr = [5, 1, 6]
arr = [5, 8, 3, 7, 9, 1]
n = len(arr)
dp = [[-2]*(n+1) for i in range(n)]


print(longIncreasing(arr, 0, -1))
print(lengthOfLIS(arr))
print(spaceOptimizeDP(arr))
print(binarySearchLong(arr))
print(longIncreasingDP(arr, 0, -1, dp))
