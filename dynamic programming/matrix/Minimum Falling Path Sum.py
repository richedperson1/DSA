import sys


"""
Using DP Approach
Time complexity : O(3^n*n)
Space complexity : O(n)
"""


def miniFallPath(matrix, i, j):
    n = len(matrix)
    if j >= n or j < 0:
        return sys.maxsize

    if i >= n:
        return 0

    first = miniFallPath(matrix, i+1, j+1)+matrix[i][j]
    second = miniFallPath(matrix, i+1, j-1)+matrix[i][j]
    third = miniFallPath(matrix, i+1, j)+matrix[i][j]
    return min(first, second, third)


def minimumFinal(mat):

    ans = sys.maxsize
    for i in range(len(mat)):
        ans = min(ans, miniFallPath(mat, 0, i))
    return ans


"""
Using DP Approach
Time complexity : O(n^2)
Space complexity : O(n^2)
"""


def miniFallPathDP(matrix, i, j, dp):
    n = len(matrix)

    if j >= n or j < 0:
        return sys.maxsize
    if i >= n:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    first = miniFallPathDP(matrix, i+1, j+1, dp)+matrix[i][j]
    second = miniFallPathDP(matrix, i+1, j-1, dp)+matrix[i][j]
    third = miniFallPathDP(matrix, i+1, j, dp)+matrix[i][j]
    final = min(first, second, third)
    dp[i][j] = final
    return final


def MinimumFallDP(matrix):
    num = len(matrix)
    ans = sys.maxsize
    dp = [[-1]*(num+1) for i in range(num+1)]
    for i in range(num):
        ans = min(ans, miniFallPathDP(matrix, 0, i, dp))
    return ans


"""
Using Tabulation DP
"""


def minimumDP_Tab(mat):
    n = len(mat)
    dp = [[sys.maxsize]*(n+2) for i in range(n+2)]

    for i in range(n):
        ans = sys.maxsize
        for j in range(n):
            val = mat[i][j]
            first = dp[i+1][j+1]+val
            second = dp[i+1][j]+val
            third = dp[i+1][j-1]+val

            ans = min(ans, first, second, third)
