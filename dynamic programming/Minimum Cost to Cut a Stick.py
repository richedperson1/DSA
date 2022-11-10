"""
Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.
The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. 
When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length 
of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.


URL : https://practice.geeksforgeeks.org/problems/rod-cutting0840/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

"""
import sys

arr = [1, 1, 1, 6]

num = 12


def minimum_cost(num, arr, total):
    if num == 0:
        return total

    if num < 0:
        return -sys.maxsize

    ans = 0
    for ind, data in enumerate(arr):
        local = num-ind-1
        # call = minimum_cost(local, arr, total+1+ind)
        ans = max(ans, minimum_cost(local, arr, total+data))

    return ans


def mini_cost_to_up(num, arr):
    if num == 0:
        return 0

    if num < 0:
        return -sys.maxsize
    ans = 0
    for i, data in enumerate(arr):
        local = num-i-1
        call = mini_cost_to_up(local, arr)
        ans = max(ans, data+call)

    return ans


def mini_cost_to_up_dp(num, arr, dp):
    if num == 0:
        return 0

    if num < 0:
        return -sys.maxsize

    if dp[num] != -95:
        return dp[num]

    ans = 0
    for i, data in enumerate(arr):
        local = num-i-1
        call = data+mini_cost_to_up_dp(local, arr, dp)
        ans = max(ans, call)
    dp[num] = ans
    return ans


arr = [1, 5, 8, 9, 10, 17, 17, 20]
num = 7

dp = [-95]*(num+1)
# # dp = ["a"]*(num+1)ṇ
print("Using simple code ", minimum_cost(num, arr, 0))
print("Using simple code bottom to top approach ", mini_cost_to_up(num, arr))
print("Using dp code bottom to top approach ",
      mini_cost_to_up_dp(num, arr, dp))
