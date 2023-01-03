"""
URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
import numpy as np
arr = [3, 3, 5, 0, 0, 3, 1, 4]


def stockPrice3(ind, flag, k):
    if k > 2 or ind >= len(arr):
        return 0

    if flag:
        karida = -arr[ind]+stockPrice3(ind+1, 0, k+1)
        kuchNahi = 0+stockPrice3(ind+1, 1, k)
        return max(kuchNahi, karida)

    else:
        becha = arr[ind]+stockPrice3(ind+1, 1, k)
        kuchNahi = 0+stockPrice3(ind+1, 0, k)
        return max(kuchNahi, becha)


def stockPrice3DP(ind, flag, k, dp):
    if k > 2 or ind >= len(arr):
        return 0

    if flag:
        karida = -arr[ind]+stockPrice3DP(ind+1, 0, k+1, dp)
        kuchNahi = 0+stockPrice3DP(ind+1, 1, k, dp)
        ans = max(kuchNahi, karida)
        dp[k][flag][ind] = ans
        return ans

    else:
        becha = arr[ind]+stockPrice3DP(ind+1, 1, k, dp)
        kuchNahi = 0+stockPrice3DP(ind+1, 0, k, dp)
        ans = max(kuchNahi, becha)
        dp[k][flag][ind] = ans
        return ans


def stockPrice3TabDP(arr):
    num = len(arr)

    kk = 3
    dp = [[[0]*(num+1) for i in range(2)] for k in range(kk+1)]
    kk = 3
    for day in range(num-1, -1, -1):
        for flag in range(2):
            for k in range(1, kk):
                if flag:
                    karido = -arr[day]+dp[k][0][day+1]
                    chodo = 0+dp[k][1][day+1]

                    dp[k][flag][day] = max(karido, chodo)
                else:
                    becho = arr[day]+dp[k-1][1][day+1]
                    chodo = 0+dp[k][0][day+1]
                    dp[k][flag][day] = max(becho, chodo)

    return dp[2][1][0]


num = len(arr)
kk = 2
dp = [[[-1]*(num+1) for i in range(2)] for k in range(kk+1)]

print(stockPrice3(0, 1, 0))
print(stockPrice3DP(0, 1, 0, dp))
print(stockPrice3TabDP(arr))
