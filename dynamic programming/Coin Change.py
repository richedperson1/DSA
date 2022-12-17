"""
maximum coin we can generate using total number
"""
import sys


def cointRequire(coins, total):
    if total < 0:
        return -sys.maxsize
    if total == 0:
        return 0

    first = cointRequire(coins, total-coins[0])+1
    second = cointRequire(coins, total-coins[1])+1
    third = cointRequire(coins, total-coins[2])+1

    return max(first, second, third)


def coinChange(coins, total):
    n = total+1
    dp = [0]*(n)
    for i in range(1, n):
        ans = -sys.maxsize
        for coin in coins:
            if i-coin >= 0:
                local = dp[i-coin]+1
                ans = max(ans, local)

        dp[i] = ans

    return dp[-1]


coins = [6, 2, 5]
amount = 9

print(cointRequire(coins, amount))
print(coinChange(coins, amount))
