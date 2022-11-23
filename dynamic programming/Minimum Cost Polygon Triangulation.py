import sys

"""
URL : https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""


def solveRecursion(val, i, j):
    if i+1 == j:
        return 0
    ans = sys.maxsize
    for k in range(i+1, j):
        local = val[k] * val[j] * val[i] + \
            solveRecursion(val, i, k)+solveRecursion(val, k, j)
        ans = min(local, ans)
    return ans


def solveDP(val, i, j, dp):
    if i+1 == j:
        return 0

    if dp[i][j] != -4:
        return dp[i][j]

    ans = sys.maxsize
    for k in range(i+1, j):
        local = val[k] * val[j] * val[i] + \
            solveDP(val, i, k, dp)+solveDP(val, k, j, dp)
        ans = min(local, ans)
    dp[i][j] = ans
    return ans
