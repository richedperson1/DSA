"""
URL : https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
"""
import sys
sys.setrecursionlimit(10**6)
num = 2


def possibleBinary(num, ind, prevZ):
    if ind >= num:
        return 1

    if prevZ == True:
        ans = possibleBinary(num, ind+1, False)
        return ans
    else:
        ans = possibleBinary(num, ind+1, False) + \
            possibleBinary(num, ind+1, True)
        return ans


"""
Time complexity : O(n)
Space complexity : O(n)
"""


def possibleBinaryDP(num, ind, prev, dp):
    if ind >= num:
        return 1

    if dp[ind][prev] != -1:
        return dp[ind][prev]

    ans = 0
    if prev == 1:
        ans = possibleBinaryDP(num, ind+1, 0, dp)
        dp[ind][prev] = ans
        return ans
    else:
        ans = possibleBinaryDP(num, ind+1, 0, dp) + \
            possibleBinaryDP(num, ind+1, 1, dp)

        dp[ind][prev] = ans
        return ans


def PossibleCount(num, prev):
    if num == 0:
        return 0
    if num == 1:
        return 2
    ans = 0
    if prev == 0:
        ans += PossibleCount(num-1, 1)
    else:
        ans += PossibleCount(num-1, 0)
        ans += PossibleCount(num-1, 1)

    return ans


def PossibleCountDP(num, prev, dp):
    if num == 0:
        return 0
    if num == 1:
        return 2
    ans = 0
    if dp[num][prev] != -1:
        return dp[num][prev]
    if prev == 0:
        ans += PossibleCountDP(num-1, 1, dp)
    else:
        ans += PossibleCountDP(num-1, 0, dp)
        ans += PossibleCountDP(num-1, 1, dp)

    dp[num][prev] = ans
    return ans


"""
Most optimize solution

Time complexity : O(n)
Space complexity : O(1)
"""


def possibleBinaryDP_optimize(num):

    dp0 = 1
    dp1 = 1
    for i in range(1, num):
        ans1 = dp0+dp1
        dp0 = dp1
        dp1 = ans1

    return dp0+dp1


num = 40
# l1 = PossibleCoun.


# print(possibleBinaryDP(num, 0, 0, dp))

ansF = []
for i in range(1, 1000):
    dp = [[-1]*(2) for i in range(i+1)]
    l1 = (PossibleCountDP(i, 0,  dp)+PossibleCountDP(i, 1,  dp))//2
    ans = possibleBinaryDP_optimize(i)
    final = l1 == ans
    ansF.append(final)

print(all(ansF))
