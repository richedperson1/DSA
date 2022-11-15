"""
Given an array of N integers arr[] where each element represents the max length of the jump that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.

URL : https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
"""
import sys
sys.setrecursionlimit(10**9)
file = "dynamic programming\\input\\minimum number jump to reach end.txt"
arr = [1, 4, 3, 2, 6, 7, 8, 1, 2]
arr = list(map(int, "2 3 1 1 2 4 2 0 1 1".split()))

with open(file) as f:
    num = []
    value = f.readlines()
    num = [int(value[0])]
    arr = list(map(int, value[1].split()))


n = len(arr)


def minimum_cost(arr, ind, n, dp):
    if ind >= n:
        return 0

    if ind+arr[ind] >= n:
        return 1

    if dp[ind] != -4:
        return dp[ind]
    ans = n+3
    for i in range(ind, ind+arr[ind]):
        local = minimum_cost(arr, i+1, n, dp)+1
        ans = min(ans, local)

    dp[ind] = ans
    return ans


dp = [-4]*(n+1)
ans = minimum_cost(arr, 0, n-1, dp)
print(ans)
