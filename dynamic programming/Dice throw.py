"""
URL : https://practice.geeksforgeeks.org/problems/dice-throw5349/1
"""

n = 3
m = 2
x = 6


def diceThrow(n, m, x):
    if (x < 0) or (n == 0 and x != 0) or (x == 0 and n != 0):
        return 0
    if x == 0 and n == 0:
        return 1

    if dp[n][x] != -1:
        return dp[n][x]
    final = 0
    for face in range(1, m+1):
        final += diceThrow(n-1, m, x-face)

    dp[n][x] = final
    return final


dp = [[-1]*(x+1) for i in range(n+1)]
print(diceThrow(n, m, x))
