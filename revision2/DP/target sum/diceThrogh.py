"""
URL : https://practice.geeksforgeeks.org/problems/dice-throw5349/1
"""


n = 13
m = 3
x = 16


def diceThrough(n, m, x):
    if x == 0 and n == 0:
        return 1
    if x == 0 and n != 0:
        return 0
    if n == 0 and x != 0:
        return 0

    ans = 0
    for tar in range(1, x+1):
        ans += diceThrough(n-1, m, x-tar)

    return ans


print(diceThrough(n, m, x))
