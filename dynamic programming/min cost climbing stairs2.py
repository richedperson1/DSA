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


def miniCostDP(arr, ind, dp):
    if ind < 0:
        return 0
    if ind == 0 or ind == 1:
        arr[ind]

    if dp[ind] != -1:
        return dp[ind]

    ans = arr[ind]+min(miniCostDP(arr, ind-1, dp), miniCostDP(arr, ind-2, dp))
    dp[ind] = ans
    return ans


"""
Tabular DP
"""


def minCostTabDP(arr):
    dp = [arr[0], arr[1]]

    n = len(arr)
    for i in range(2, n):
        ans = arr[i]+min(dp[i-1], dp[i-2])
        dp.append(ans)
    return min(dp[-1], dp[-2])


"""
Most optimize DP solution
"""


def minCostTabDP2(arr):

    n = len(arr)
    first = arr[0]
    second = arr[1]
    ans = 0
    for i in range(2, n):
        ans = arr[i]+min(first, second)
        first = second
        second = ans
    return min(first, second)


arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
arr = [10, 15, 20]


print(miniCost2(arr, 0, True))
n = len(arr)-1
dp = [-1]*(n+2)
l1 = min(miniCostDP(arr, n, dp), miniCostDP(arr, n-1, dp))
print(l1)
print(minCostTabDP(arr))
print(minCostTabDP2(arr))
