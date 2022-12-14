"""
URL :  https://leetcode.com/problems/house-robber/description/
"""

"""
Brute force approach 

Time complexity : O(2^n)
Space complexity : O(n)

"""


def robber(arr, ind):
    if ind >= len(arr):
        return 0

    firstChoice = robber(arr, ind+2)+arr[ind]
    secondChoice = robber(arr, ind+1)

    return max(firstChoice, secondChoice)


"""
Better approach

Time complexity : O(n)
Space complexity : O(2n)
"""


def robberDP(arr, ind, dp):
    # base case remain same for both approach[Better approach and Brute force approach ]
    if ind >= len(arr):
        return 0

    if dp[ind] != -1:
        return dp[ind]

    firstChoice = robberDP(arr, ind+2, dp)+arr[ind]
    secondChoice = robberDP(arr, ind+1, dp)+0
    maxi = max(firstChoice, secondChoice)

    dp[ind] = maxi
    return maxi


"""
Better approach

Time complexity : O(n)
Space complexity : O(2n)
"""


def robberDP_tab(arr):
    n = len(arr)
    dp = [0]*(n+2)

    for house in range(n-1, -1, -1):
        first = dp[house+2]+arr[house]
        second = dp[house+1]
        maxi = max(first, second)
        dp[house] = maxi
    return dp[0]


"""
Optimize approach

Time complexity : O(n)
Space complexity : O(1)
"""


def robberDP_tabOptimize(arr):
    n = len(arr)
    first = 0
    second = 0
    for house in range(n-1, -1, -1):
        l1 = second+arr[house]
        l2 = first
        maxi = max(l1, l2)
        second = first
        first = maxi
    return max(first, second)


arr = [1, 2, 3, 12, 3, 4, 100]
n = len(arr)
print(robber(arr, 0))
dp = [-1]*(n)

print(robberDP(arr, 0, dp))
print(robberDP_tab(arr))
print(robberDP_tabOptimize(arr))
