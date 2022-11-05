
"""
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


n = 36
dp = [0]*(n+1)
num = [17, 10, 5]
ans = mini_cost_dp(num, n, dp)
print(ans)
