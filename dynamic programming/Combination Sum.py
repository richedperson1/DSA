
"""
Combinational sum 

URL : https://www.codingninjas.com/codestudio/problems/number-of-ways_3755252
"""
import sys

"""
Time complexity : O(n^k)
space complexity : O(n)
"""


def combinationSum(arr, tar):
    if tar == 0:
        return 1

    ans = 0
    for ind, data in enumerate(arr):
        newTar = tar - data
        if newTar >= 0:
            ans += combinationSum(arr, newTar)
    return ans


"""
Time complexity : O(n*target)
space complexity : O(n)
"""


def combinationSumDP(arr, tar, dp):
    if tar == 0:
        return 1

    if dp[tar] != -1:
        return dp[tar]
    ans = 0
    for ind, data in enumerate(arr):
        newTar = tar - data
        if newTar >= 0:
            ans += combinationSumDP(arr, newTar, dp)

    dp[tar] = ans
    return ans


"""
Time complexity : O(n*target)
space complexity : O(n)
"""


def combinationSumTabDP(arr, target):
    dp = [0]*(target+1)
    dp[0] = 1
    for tar in range(1, target+1):
        ans = 0
        for ind, data in enumerate(arr):
            newTar = tar-data
            if newTar >= 0:
                ans += dp[newTar]
        dp[tar] = ans

    return dp[-1]


arr = [1, 2, 5]
k = 5
dp = [-1]*(k+1)
print(combinationSum(arr, k))
print(combinationSumTabDP(arr, k))
print(combinationSumDP(arr, k, dp))
