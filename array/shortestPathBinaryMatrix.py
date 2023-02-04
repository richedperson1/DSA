
"""
URL : https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
import sys


"""
Time complexity : O(3^n)
space complexity : O(n)
"""


def pathBinary(arr, row, col):
    n = len(arr)
    if row > n or col > n:
        return sys.maxsize
    if row == (n-1) and col == (n-1):
        return 1

    if arr[row][col] == 1:
        return sys.maxsize

    l1 = pathBinary(arr, row+1, col)
    l2 = pathBinary(arr, row+1, col+1)
    l3 = pathBinary(arr, row, col+1)

    return min(l1, l2, l3)+1


"""
Time complexity : O(3^n)
space complexity : O(n)
"""


def pathBinaryDP(arr, row, col, dp):
    n = len(arr)
    if row > n or col > n:
        return sys.maxsize
    if row == (n-1) and col == (n-1):
        return 1

    if arr[row][col] == 1:
        return sys.maxsize

    if dp[row][col] != -1:
        return dp[row][col]
    l1 = pathBinaryDP(arr, row+1, col, dp)
    l2 = pathBinaryDP(arr, row+1, col+1, dp)
    l3 = pathBinaryDP(arr, row, col+1, dp)

    dp[row][col] = min(l1, l2, l3)+1

    return dp[row][col]


arr = [[0, 1], [1, 0]]
n = len(arr)
dp = [[-1]*n for i in range(n)]
print(pathBinary(arr, 0, 0))
print(pathBinaryDP(arr, 0, 0, dp))
