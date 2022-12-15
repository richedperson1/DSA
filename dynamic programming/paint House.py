"""
URL : https://www.geeksforgeeks.org/minimize-cost-of-painting-n-houses-such-that-adjacent-houses-have-different-colors/

URL : https://www.interviewbit.com/problems/paint-house/
"""

import sys
arr = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]

"""
Method 1

Brute force approach
Time complexity : O(2^n)
Space complexity : O(n)
"""


def paintMin(arr, ind, prev):
    n = len(arr)
    if ind >= n:
        return 0

    ans = sys.maxsize
    for i in range(3):
        if prev != i:
            l1 = paintMin(arr, ind+1, i)+arr[ind][i]
            ans = min(ans, l1)
    return ans


def paintMinimumHouse(arr):
    final = sys.maxsize
    for i in range(3):
        local = paintMin(arr, 0, i)
        final = min(final, local)

    return final


"""
Method 2

Optimize Better approach
Time complexity : O(n)
Space complexity : O(n)
"""


def paintMinDP(arr, ind, prev, dp):
    n = len(arr)
    if ind >= n:
        return 0

    if dp[ind][prev] != -1:
        return dp[ind][prev]
    ans = sys.maxsize
    for i in range(3):
        if prev != i:
            l1 = paintMinDP(arr, ind+1, i, dp)+arr[ind][i]
            ans = min(ans, l1)

    dp[ind][prev] = ans
    return ans


def minCost(arr):
    # Write your code here.
    final = sys.maxsize
    n = len(arr)
    dp = [[-1]*(4) for i in range(n+1)]
    for i in range(3):
        local = paintMinDP(arr, 0, i, dp)
        final = min(final, local)

    return final


"""
Method 3

Optimize Better approach
Time complexity : O(n)
Space complexity : O(n)

Tabular DP
"""


def paint_min_tab(arr):
    n = len(arr)

    dp = [[0]*3 for i in range(n)]

    for i in range(3):
        dp[0][i] = arr[0][i]

    for house in range(1, n):
        for color in range(3):
            ans = sys.maxsize
            for backColor in range(3):
                if color != backColor:
                    local = dp[house-1][backColor]+arr[house][color]
                    ans = min(local, ans)

            dp[house][color] = ans

    return min(dp[-1])


"""
Method 3

Most Optimize approach
Time complexity : O(n)
Space complexity : O(1)

Tabular DP
"""


def paint_min_optimize(arr):
    n = len(arr)
    dpBack = [0]*3
    DpCurr = [0]*3
    for i in range(3):
        dpBack[i] = arr[0][i]
    for house in range(1, n):
        for color in range(3):
            ans = sys.maxsize
            for backColor in range(3):
                if color != backColor:
                    local = dpBack[backColor]+arr[house][color]
                    ans = min(local, ans)

            DpCurr[color] = ans
        """
        If we used
        dpBack = DpCurr
        Then both list pointing each other and cause an error 
        
        Both dpBack and DpCurr will change at same.
        """
        dpBack = DpCurr.copy()  # Deep copy will happen

    return min(DpCurr)


arr = [[1, 2, 3], [10, 11, 12]]
arr = [[8, 4, 7], [7, 8, 2], [6, 9, 8], [7, 6, 4], [7, 7, 8]]
print(paintMinimumHouse(arr))
print(minCost(arr))
print(paint_min_tab(arr))
print(paint_min_optimize(arr))


"""
8 4 7 
7 8 2 
6 9 8 
7 6 4 
7 7 8 
"""
