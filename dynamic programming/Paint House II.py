"""
Premium URL :  https://leetcode.com/problems/paint-house-ii/
Note : This url for premium customer of leetcode if you find similar problem please suggect link 

URL : https://www.pepcoding.com/resources/online-java-foundation/dynamic-programming-and-greedy/paint-house-many-colors-official/ojquestion
"""
import sys


"""
Brute force approach 
Time complexity : O(k*n^n)
space complexity : O(n)
"""


def paintHousesolve(arr, ind, prev):
    n = len(arr)
    if ind >= n:
        return 0

    k = len(arr[0])
    ans = sys.maxsize
    for color in range(k):
        if color != prev:
            local = paintHousesolve(arr, ind+1, color)+arr[ind][color]
            ans = min(local, ans)
    return ans


def paintHouse2(arr):
    n = len(arr[0])
    finalAns = sys.maxsize

    for first in range(n):
        local = paintHousesolve(arr, 0, first)
        finalAns = min(finalAns, local)
    return finalAns


"""
DP approach 
Time complexity : O(k*n)
space complexity : O(n*k)
"""


def paintHousesolveDP(arr, ind, prev, dp):
    n = len(arr)
    if ind >= n:
        return 0

    if dp[ind][prev] != -1:
        return dp[ind][prev]
    k = len(arr[0])
    ans = sys.maxsize
    for color in range(k):
        if color != prev:
            local = paintHousesolveDP(arr, ind+1, color, dp)+arr[ind][color]
            ans = min(local, ans)

    dp[ind][prev] = ans
    return ans


def paintHouse2DP(arr):
    n = len(arr[0])
    finalAns = sys.maxsize
    dp = [[-1]*n for i in range(len(arr)+1)]
    for first in range(n):
        local = paintHousesolveDP(arr, 0, first, dp)
        finalAns = min(finalAns, local)
    return finalAns


"""
Tabular DP approach 

Time complexity : O(k*n)
space complexity : O(n*k)

"""


def paintHouse2DPTab(arr):
    n = len(arr)
    k = len(arr[0])
    dp = [[0]*k for i in range(n)]

    for color in range(k):
        dp[0][color] = arr[0][color]
    for house in range(1, n):

        for color in range(k):
            ans = sys.maxsize
            for currColor in range(k):
                if color != currColor:
                    backHouse = dp[house-1][currColor]+arr[house][color]
                    ans = min(ans, backHouse)
            dp[house][color] = ans
    return min(dp[-1])


"""
Tabular DP approach 

Time complexity : O(k*n)
space complexity : O(k)
"""


def paintHouse2DPTabObtimize(arr):
    n = len(arr)
    k = len(arr[0])

    backDP = [0]*k
    currDP = [0]*k
    for color in range(k):
        backDP[color] = arr[0][color]
    for house in range(1, n):

        for color in range(k):
            ans = sys.maxsize
            for currColor in range(k):
                if color != currColor:
                    backHouse = backDP[currColor]+arr[house][color]
                    ans = min(ans, backHouse)
            currDP[color] = ans
        backDP = currDP.copy()
    return min(currDP)


# arr =
arr = [[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]]

print(paintHouse2(arr))
print(paintHouse2DP(arr))
print(paintHouse2DPTab(arr))
print(paintHouse2DPTabObtimize(arr))
