"""
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1 
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.


"""
"""
URL : https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
"""


"""
Time complexity : O(2^n)
Space complexity : O(n) : stack spance only
"""




import sys
def sumset(arr, sumi, ind):
    n = len(arr)
    # Base condition
    if sumi == 0:
        return True
    if ind >= n:
        if sumi == 0:
            return True
        return False

    local = sumi - arr[ind]
    ans = False
    if local >= 0:
        ans = sumset(arr, local, ind+1)

    anss = False

    anss = sumset(arr, sumi, ind+1)
    return ans or anss


def sumsetDP(arr, sumi, ind, dp):
    n = len(arr)
    # Base condition
    if sumi == 0:
        return True
    if ind >= n:
        if sumi == 0:
            return True
        return False

    if dp[ind][sumi] != -5:
        return dp[ind]

    local = sumi - arr[ind]
    if local >= 0:
        ans1 = sumsetDP(arr, local, ind+1, dp)
        ans2 = sumsetDP(arr, sumi, ind+1, dp)
        dp[ind][local] = ans1
        dp[ind][sumi] = ans2
        return ans1 or ans2

    final = sumsetDP(arr, sumi, ind+1, dp)
    dp[ind][sumi] = final
    return final


arr = [13, 34, 4, 12, 5]

n = len(arr)

for sumi in range(1, 20):
    l1 = sumset(arr, sumi, 0)
    dp = [[-5]*(sumi+1) for i in range(n+1)]
    l2 = sumsetDP(arr, sumi, 0, dp)
    print(l1 == l2)
