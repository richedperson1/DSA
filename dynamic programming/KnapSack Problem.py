"""
URL : https://www.codingninjas.com/codestudio/problems/0-1-knapsack_920542 
"""

"""
Brute force approach 

Time complexity : O(2^n)
Space complexity : O(n)
"""


def maximum_rob(weight, value, w, ind, local, ans):
    if ind >= len(weight) or w <= 0:
        ans.append(sum(local))
        return
    if w-weight[ind] >= 0:
        maximum_rob(weight, value, w -
                    weight[ind], ind+1, local+[value[ind]], ans)

    maximum_rob(weight, value, w, ind+1, local, ans)


"""
Brute force better approach 

Time complexity : O(2^n)
Space complexity : O(n)

"""


def maximum_rob_better(weight, value, w, ind, local, ans):
    if ind >= len(weight) or w <= 0:
        ans.append(local)
        return
    if w-weight[ind] >= 0:
        maximum_rob_better(weight, value, w -
                           weight[ind], ind+1, local+value[ind], ans)

    maximum_rob_better(weight, value, w, ind+1, local, ans)


"""
Brute force optimize approach
"""


def maximum_rob_mod(weight, value, w, ind):
    if ind >= len(weight):
        return 0

    inc = 0
    exc = 0
    local_check = w-weight[ind]
    if local_check >= 0:
        inc = value[ind]+maximum_rob_mod(weight, value, local_check, ind+1)

    exc = maximum_rob_mod(weight, value, w, ind+1)
    return max(inc, exc)


"""
Most optimize solution

Time complexity : O(n)
Space complexity : O(n)
"""
dp_count = 0


def maximum_rob_dp(weight, value, w, ind, dp):
    if w == 0:
        return 0

    if ind == 0:
        if weight[0] <= w:
            return value[0]
        return 0

    if dp[ind][w] != -5:
        return dp[ind][w]
    inc = 0
    exc = 0
    local_check = w-weight[ind]
    if local_check >= 0:
        inc = value[ind]+maximum_rob_dp(weight, value, local_check, ind-1, dp)

    exc = maximum_rob_dp(weight, value, w, ind-1, dp)
    maxi = max(inc, exc)
    dp[ind][w] = maxi
    return maxi


def maximum_rob_mod_dp(weight, value, w, ind, dp):
    if ind >= len(weight):
        return 0

    if dp[ind] != -5:
        return dp[ind]
    inc = 0
    exc = 0
    local_check = w-weight[ind]
    if local_check >= 0:
        inc = value[ind] + \
            maximum_rob_mod_dp(weight, value, local_check, ind+1, dp)

    exc = maximum_rob_mod_dp(weight, value, w, ind+1, dp)
    maxi = max(inc, exc)
    dp[ind] = maxi
    return maxi


# Test case
weight = list(map(int, "57 95 13 29 1 99 34 77 61 23 24 70 73 88 33 61 43 5 41 63 8 67 20 72 98 59 46 58 64 94 97 70 46 81 42 7 1 52 20 54 81 3 73 78 81 11 41 45 18 94 24 82 9 19 59 48 2 72".split()))
value = list(map(int, "83 84 85 76 13 87 2 23 33 82 79 100 88 85 91 78 83 44 4 50 11 68 90 88 73 83 46 16 7 35 76 31 40 49 65 2 18 47 55 38 75 58 86 77 96 94 82 92 10 86 54 49 65 44 77 22 81 52".split()))

# value = [1, 2, 3]
# weight = [4, 5, 1]
w = 4
n = len(weight)
dp = [[-5]*(w+1)]*(n+1)

dp_ = [-5]*(n+1)
print(maximum_rob_dp(weight, value, w, n-1, dp))
print(maximum_rob_mod_dp(weight, value, w, 0, dp_))
