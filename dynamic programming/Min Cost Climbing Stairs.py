from typing import *


"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


url : https://leetcode.com/problems/min-cost-climbing-stairs/

answer create : rutvikjaiswal195@gmail.com
"""
arr = [3, 10, 2, 4, 8, 10]

"""
Naive algorithms
Time complexity : O(2^n)
space complexity : O(n)
"""


def minCostClimbingStairs_recursion(cost, n):
    if n == 1 or n == 0:
        return cost[n]
    l1 = minCostClimbingStairs_recursion(cost, n-1)
    l2 = minCostClimbingStairs_recursion(cost, n-2)
    ans = min(l1, l2)+cost[n]
    return ans


num = len(arr)
ans = min(minCostClimbingStairs_recursion(arr, num-1),
          minCostClimbingStairs_recursion(arr, num-2))

print(ans)


"""
Better approach 
Time complexity : O(n)
spce complexity : O(2n)
"""


def using_DP_memo(cost, n, final):
    if n == 1 or n == 0:
        return cost[n]

    if final[n] != 0:
        return final[n]

    final[n-1] = using_DP_memo(cost, n-1, final)
    final[n-2] = using_DP_memo(cost, n-2, final)
    # l1 = minCostClimbingStairs_recursion(cost, n-1, final)
    l1 = final[n-1]
    l2 = final[n-2]
    ans = min(l1, l2) + cost[n]
    return ans


final = [0]*num
l1 = using_DP_memo(arr, num-1, final)
l2 = using_DP_memo(arr, num-2, final)
print(min(l1, l2))


"""
Better Optimize solution 

Time complexity : O(n)
space complexity: O(n)
"""


def minCostClimbingStairs_with_space(arr: List[int]) -> int:
    n = len(arr)
    dp = [0]*n
    dp[0] = arr[0]
    dp[1] = arr[1]
    for i in range(2, n):
        mini_ans = min(dp[i-1], dp[i-2])+arr[i]
        dp[i] = mini_ans

    return min(dp[-2:])


"""
Most optimize solution

Time complexity : O(n)
space complexity: O(1)
"""


def minCostClimbingStairs_without_space(arr: List[int]) -> int:
    n = len(arr)
    first = arr[0]
    second = arr[1]
    i = 2
    while i < n:
        # for i in range(2,n):
        ans = min(first, second)+arr[i]
        first = second
        second = ans
        i += 1
    return min(first, second)
