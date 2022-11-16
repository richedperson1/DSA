"""
Given an array of N integers arr[] where each element represents the max length of the jump that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.

Note: Return -1 if you can't reach the end of the array.

URL : https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
"""
import sys
sys.setrecursionlimit(10**9)
file = "dynamic programming\\input\\minimum number jump to reach end.txt"
arr = [1, 4, 3, 2, 6, 7, 8, 1, 2]
arr = list(map(int, "5 9 3 2 1 0 2 3 3 1 0 0".split()))

# with open(file) as f:
#     num = []
#     value = f.readlines()
#     num = [int(value[0])]
#     arr = list(map(int, value[1].split()))


n = len(arr)

# 5 9 3 2 1 0 2 3 3 1 0 0


def minimum_jump_brute_force(arr, ind, n):
    if ind >= n:
        return 0

    ans = sys.maxsize
    for i in range(ind, ind+arr[ind]):
        ans = min(ans, minimum_jump_brute_force(arr, i+1, n)+1)

    return ans


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


def minimum_jump_optimize(arr):
    if len(arr) <= 1:
        return 0

    if arr[0] == 0:
        return 0

    maxReach = arr[0]
    step = arr[0]
    num = len(arr)
    jump = 1
    for i in range(1, n):
        if i == n-1:
            return jump

        step -= 1
        if step == 0:
            if i >= maxReach:
                return -1
            step = maxReach-i
    return jump


arr = [1, 3, 5, 7, 9, 3]
print(minimum_jump_brute_force(arr, 0, len(arr)-1))
