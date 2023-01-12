"""
URL : https://practice.geeksforgeeks.org/problems/dice-throw5349/1
"""


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


def diceThrowTab(n, m, x):
    dp = [[0]*(x+1) for i in range(n+1)]
    dp[0][0] = 1

    for nn in range(1, n+1):
        for tar in range(1, x+1):
            final = 0
            for face in range(1, m+1):
                if tar-face >= 0:
                    final += dp[nn-1][tar-face]

            dp[nn][tar] = final

    return dp[n][-1]


def diceThrowTabOpt(n, m, x):
    # dp = [[0]*(x+1) for i in range(n+1)]
    dp[0][0] = 1

    dpCurr = [0]*(x+1)
    dpBack = [0]*(x+1)
    dpBack[0] = 1
    for nn in range(1, n+1):
        for tar in range(1, x+1):
            final = 0
            for face in range(1, m+1):
                if tar-face >= 0:
                    final += dpBack[tar-face]

            dpCurr[tar] = final
        dpBack = dpCurr.copy()

    return dpCurr[-1]


n = 13
m = 3
x = 16

dp = [[-1]*(x+1) for i in range(n+1)]
print(diceThrow(n, m, x))
print(diceThrowTab(n, m, x))
print(diceThrowTabOpt(n, m, x))
