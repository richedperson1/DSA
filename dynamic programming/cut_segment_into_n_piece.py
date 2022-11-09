"""
You are given an integer ‘N’ denoting the length of the rod. You need to determine the maximum number 
of segments you can make of this rod provided that each segment should be in array arr

Input: 

arr = [3, 4, 5, 6]
num = 10

Output: 
3
"""


import sys
arr = [3, 4, 5, 6]

num = 10

"""
Naive approach

Time complexity : O(k^n)
    k: size of array

space complexity : O(n)
"""


def cut_rod(num, arr):
    if num == 0:
        return 0
    if num < 0:
        return -sys.maxsize

    ans = 0
    for i, data in enumerate(arr):
        local = num-data
        ans = max(ans, cut_rod(local, arr)+1)

    return ans


print(cut_rod(num, arr))


def cut_rod_dp(num, dp, arr):
    if num == 0:
        return 0

    if num < 0:
        return -sys.maxsize

    if dp[num] != "a":
        return dp[num]
    ans = 0
    for i, data in enumerate(arr):
        local = num-data
        ans = max(ans, cut_rod_dp(local, dp, arr)+1)

    dp[num] = ans
    return ans


dp = ["a"]*(num+1)

print(cut_rod_dp(num, dp, arr))
