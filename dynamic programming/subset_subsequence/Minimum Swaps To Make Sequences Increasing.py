"""
URL : https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
"""
import sys
nums1 = [1, 3, 5, 4]
nums2 = [1, 2, 3, 7]


"""
Recursive approach

Time complexity : O(2^n)
Space complexity : O(n) : stack spance only
"""


def miniMumSwap(num1, num2, ind, swapped):
    if ind >= len(num1):
        return 0

    prev1 = num1[ind-1]
    prev2 = num2[ind-1]
    if swapped:
        prev1, prev2 = prev2, prev1

    ans = sys.maxsize
    if num1[ind] > prev1 and num2[ind] > prev2:
        ans = miniMumSwap(num1, num2, ind+1, 0)

    if num1[ind] > prev2 and num2[ind] > prev1:
        ans = min(ans, miniMumSwap(num1, num2, ind+1, 1)+1)

    return ans


"""
DP approach

Time complexity : O(n)
Space complexity : O(n) 
"""


def minimumSwapDP(num1, num2, ind, swapped, dp):
    if ind >= len(num1):
        return 0

    if dp[ind][swapped] != -1:
        return dp[ind][swapped]

    ans = sys.maxsize
    prev1 = num1[ind-1]
    prev2 = num2[ind-1]
    if swapped:
        prev1, prev2 = prev2, prev1
    if num1[ind] > prev1 and num2[ind] > prev2:
        ans = minimumSwapDP(num1, num2, ind+1, 0, dp)

    if num1[ind] > prev2 and num2[ind] > prev1:
        ans = min(ans, minimumSwapDP(num1, num2, ind+1, 1, dp)+1)

    dp[ind][swapped] = ans
    return ans


"""
DP Tab approach

Time complexity : O(n)
Space complexity : O(n) 
"""


def minimumSwapTabDP(num1, num2):
    n = len(num1)
    dp = [[0]*2 for i in range(n+2)]

    for ind in range(n-1, 0, -1):
        for swapped in range(1, -1, -1):
            prev1 = num1[ind-1]
            prev2 = num2[ind-1]
            ans = sys.maxsize
            if swapped:
                prev1, prev2 = prev2, prev1

            if num1[ind] > prev1 and num2[ind] > prev2:
                ans = dp[ind+1][0]
            if num1[ind] > prev2 and num2[ind] > prev1:
                ans = min(ans, 1+dp[ind+1][1])

            dp[ind][swapped] = ans

    return dp[1][0]


"""
DP Tab approach

Time complexity : O(n)
Space complexity : O(1) 
"""


def minimumSwapTabOptDP(num1, num2):
    n = len(num1)
    dpNext = [0]*2
    dpCurr = [0]*2
    for ind in range(n-1, 0, -1):
        for swapped in range(1, -1, -1):
            prev1 = num1[ind-1]
            prev2 = num2[ind-1]
            ans = sys.maxsize
            if swapped:
                prev1, prev2 = prev2, prev1

            if num1[ind] > prev1 and num2[ind] > prev2:
                ans = dpNext[0]
            if num1[ind] > prev2 and num2[ind] > prev1:
                ans = min(ans, 1+dpNext[1])

            dpCurr[swapped] = ans
        dpNext = dpCurr.copy()

    return dpNext[0]


num1 = [3, 3, 8, 9, 10]
num2 = [1, 7, 4, 6, 8]

nums1 = [-1]+nums1
nums2 = [-1]+nums2


n = len(nums1)
dp = [[-1]*2 for i in range(n+2)]

print(miniMumSwap(nums1, nums2, 1, 0))

print(minimumSwapDP(nums1, nums2, 1, 0, dp))
print(minimumSwapTabDP(nums1, nums2))
print(minimumSwapTabOptDP(nums1, nums2))
