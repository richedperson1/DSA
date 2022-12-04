"""
URL : https://leetcode.com/problems/climbing-stairs/
"""

"""
Time complexity : O(2^n)
space complexity : O(n)
"""


def countWay(n):
    if n <= 0:
        return 0
    if n <= 2:
        return n

    return countWay(n-1)+countWay(n-2)


"""
Time complexity : O(n)
space complexity : O(n)
"""


def countHelper(n, dp):
    if n <= 0:
        return 1
    if n <= 2:
        return n
    if dp[n] != 0:
        return dp[n]
    dp[n] = countHelper(n-1, dp)+countHelper(n-2, dp)
    return dp[n]


def countDistinctWays2(nStairs: int) -> int:
    #  Write your code here.
    dp = [0]*(nStairs+1)
    return countHelper(nStairs, dp)


"""
Time complexity : O(n)
space complexity : O(n)
"""


def countDistTab(num):
    dp = [0]
    dp.append(1)
    dp.append(2)
    for i in range(3, num+1):
        first = dp[i-1]
        second = dp[i-2]
        dp.append(first+second)
    return dp[-1]


"""
Time complexity : O(n)
space complexity : O(1)
"""


def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    if nStairs == 1:
        return 1
    first = 1
    second = 2
    for num in range(3, nStairs+1):
        third = first+second
        first = second
        second = third
    return second


n = 49
n = 10
print(countDistinctWays2(n))
print(countDistTab(n))
print(countDistinctWays(n))
