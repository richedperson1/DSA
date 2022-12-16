"""
URL : https://leetcode.com/problems/coin-change/
"""
import sys
coins = [1, 2, 5]
amount = 9


def cointRequire(coins, total):
    if total < 0:
        return sys.maxsize
    if total == 0:
        return 0

    first = cointRequire(coins, total-coins[0])+1
    second = cointRequire(coins, total-coins[1])+1
    third = cointRequire(coins, total-coins[2])+1

    return min(first, second, third)


print(cointRequire(coins, amount))
