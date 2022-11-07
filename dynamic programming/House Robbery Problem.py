"""
You are given an array/list of non-negative integers 'ARR' representing the amount of money of each house.
Your task is to return the maximum amount of money Mr. X can rob tonight without alerting the police.


url : https://www.codingninjas.com/codestudio/problems/house-robber_839733

"""


arr = [2, 3, 2]


def maximum_rob(arr, n, dp):
    if n == 0:
        return arr[0]
    if n < 0:
        return 0
    if dp[n] != 0:
        return dp[n]
    l1 = maximum_rob(arr, n-2, dp)+arr[n]
    l2 = maximum_rob(arr, n-1, dp)
    ans = max(l1, l2)
    dp[n] = ans
    return ans


first_one = arr[1:]
last_one = arr[:-1]
n1 = len(first_one)-1
n2 = len(last_one)-1

dp = [0]*(n1+1)
l1 = maximum_rob(first_one, n1, dp)
l2 = maximum_rob(last_one, n2, dp)
ans = max(l1, l2)
print(ans)
