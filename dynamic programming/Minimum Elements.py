
"""

URL {Leetcode}     : https://leetcode.com/problems/coin-change/ 
URL {CodingStudio} : https://www.codingninjas.com/codestudio/problems/minimum-elements_3843091

You are given an array of N distinct integers and an integer X representing the target sum. 
You have to tell the minimum number of elements you have to take to reach the target sum X.
"""

import sys
num = [1, 2, 3]
n = 18

count = 0


"""
Top to bottom approach 
"""
# Method 1


def minimum_cost(num, x, cost):
    global count
    count += 1
    if x < 0:
        return 651161
    if x == 0:
        return cost

    ans = 165681
    for i in num:
        if (x-i) >= 0:
            l1 = minimum_cost(num, x-i, cost+1)
            ans = min(l1, ans)

    return ans

# Method 2


"""
Time complexity : O(m^n)
Space complexity : O(n)   ie. only stack space
"""


def minCoin(coins, totals):
    if totals <= 0:
        return 0

    ans = sys.maxsize
    for coin in coins:
        newTotal = totals-coin
        if newTotal >= 0:
            finalC = minCoin(coins, newTotal)+1
            ans = min(ans, finalC)

    return ans

    # out = minimum_cost(num, n, 0)
    # print(count)


count = 0


# def minimum_cost_dp(num, x, cost):
#     global dp, count
#     count += 1
#     if x < 0:
#         return 651161
#     if x == 0:
#         return cost

#     if dp[x] != 0:
#         return dp[x]+cost

#     ans = 165681
#     for i in num:
#         if (x-i) >= 0:
#             l1 = minimum_cost_dp(num, x-i, cost+1)
#             ans = min(l1, ans)

#     dp[x] = ans
#     return ans


# num = [1, 2, 3]
# n = 18
# dp = [0]*(n+1)

# out = minimum_cost(num, n, 0)
# print("Count using dp is : ", count)


int_max = sys.maxsize

count = 0


# ----------------------------------------------------
def mini_cost__(num, x, dp):
    global int_max
    if x == 0:
        return 0

    if x < 0:
        return int_max

    if dp[x] != 0:
        return dp[x]
    ans = int_max
    for i in num:
        l1 = mini_cost_dp(num, x-i, dp)
        if l1 != int_max:
            ans = min(ans, l1+1)

    dp[x] = ans
    return ans
# ----------------------------------------------------


def mini_cost_dp(num, x, dp):
    global int_max
    if x == 0:
        return 0

    if x < 0:
        return int_max

    if dp[x] != 0:
        return dp[x]

    ans = int_max
    for i in num:
        l1 = mini_cost_dp(num, x-i, dp)
        if l1 != int_max:
            ans = min(ans, l1+1)

    dp[x] = ans
    return ans


def minCoinDP(coins, totals, dp):
    if totals <= 0:
        return 0

    if dp[totals] != -1:
        return dp[totals]

    ans = sys.maxsize
    for coin in coins:
        newTotal = totals-coin
        if newTotal >= 0:
            local = minCoinDP(coins, newTotal, dp)+1
            ans = min(ans, local)

    dp[totals] = ans
    return ans


"""
 Using tabulation DP

"""


def minCoinDP_Tab(coins, totals):
    dp = [0]

    for total in range(1, totals+1):
        ans = sys.maxsize
        for coin in coins:
            newTotal = total-coin
            if newTotal >= 0:
                local = dp[newTotal]+1
                ans = min(ans, local)

        dp.append(ans)
    return dp


n = 3
dp = [0]*(n+1)
num = [2, 4, 10, 5]
print(mini_cost_dp(num, n, dp))
print(minCoinDP_Tab(num, n))
dp = [-1]*(n+1)
print(minCoinDP(num, n, dp))
