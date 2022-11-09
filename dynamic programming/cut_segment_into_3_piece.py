
"""
You are given an integer ‘N’ denoting the length of the rod. You need to determine the maximum number 
of segments you can make of this rod provided that each segment should be of the length 'X', 'Y', or 'Z'

URL : https://www.codingninjas.com/codestudio/problems/cut-into-segments_1214651

video link : https://www.youtube.com/watch?v=MFAAZW2znv8&list=PLDzeHZWIZsTomOPnCiU3J95WufjE36wsb&index=6&t=129s 

"""
import sys


"""
Time complexity : O(3^n)
Space Complexity: O(n)
"""


def cutSegments(n, x, y, z):
    if n == 0:
        return 0
    if n < min(x, y, z):
        return -sys.maxsize

    first = 0
    second = 0
    third = 0
    if n-x >= 0:
        first = cutSegments(n-x, x, y, z)+1
        # if first >= 0:
        #     first += 1

    if n-y >= 0:
        second = cutSegments(n-y, x, y, z)+1
        # if second >= 0:
        #     second += 1

    if n-z >= 0:
        third = cutSegments(n-z, x, y, z)+1
        # if third >= 0:
        #     third += 1

    if first+second+third == 0:
        return -sys.maxsize

    return max(first, second, third)


# num = 7

# ans = cutSegments(num, 5, 2, 2, dp=dp_)
# print(ans)


"""
Time complexity : O(n)
Space Complexity: O(n)
"""
num = 7
dp = ["a"]*(num+1)


def cutSegments_dp(n, x, y, z, dp):
    if n < 0:
        return -sys.maxsize
    if n == 0:
        return 0

    if dp[n] != "a":
        return dp[n]
    f = cutSegments_dp(n-x, x, y, z, dp)+1
    s = cutSegments_dp(n-y, x, y, z, dp)+1
    t = cutSegments_dp(n-z, x, y, z, dp)+1
    ans = max(f, s, t)
    dp[n] = ans
    return ans


print(cutSegments_dp(num, 3, 3, 5, dp))
