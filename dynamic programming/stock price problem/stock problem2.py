"""
URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

"""
Using recursive approach

Time complexity : O(2^n)
Space complexity : O(n)

"""

arr = [7, 1, 5]


def maximumProfit(ind, buyF):
    if ind >= len(arr):
        return 0

    if buyF:
        karido = maximumProfit(ind+1, 0)-arr[ind]
        khatam = maximumProfit(ind+1, 1)
        return max(karido, khatam)

    else:
        becho = maximumProfit(ind+1, 1)+arr[ind]
        chodo = maximumProfit(ind+1, 0)

        return max(becho, chodo)


"""
Using DP approach

Time complexity : O(n)
Space complexity : O(n)

"""


def maximumProfitDP(ind, buyf, dp):
    if ind >= len(arr):
        return 0

    if dp[ind][buyf] != -1:
        return dp[ind][buyf]

    if buyf:
        karido = -arr[ind]+maximumProfitDP(ind+1, 0, dp)
        rahenedo = 0+maximumProfitDP(ind+1, 1, dp)
        maxi = max(karido, rahenedo)
        dp[ind][buyf] = maxi
        return maxi

    else:
        becho = arr[ind]+maximumProfitDP(ind+1, 1, dp)
        rahenedo = 0+maximumProfitDP(ind+1, 0, dp)
        maxi = max(becho, rahenedo)
        dp[ind][buyf] = maxi
        return maxi


def maximumProfitTabDP(arr):
    n = len(arr)
    dp = [[0]*2 for i in range(n+2)]
    buyf = 1
    for day in range(n-1, -1, -1):
        for operation in range(2):
            if operation:
                karido = -arr[day]+dp[day+1][0]
                chodo = dp[day+1][1]
                maxi = max(karido, chodo)
                dp[day][operation] = maxi
            else:
                becho = arr[day]+dp[day+1][1]
                chodo = dp[day+1][0]
                maxi = max(becho, chodo)
                dp[day][operation] = maxi

    return dp[0][1]


def maximumProfitTabSpaceOptDP(arr):
    n = len(arr)
    dpNext = [0, 0]
    for day in range(n-1, -1, -1):
        dpCurr = [0, 0]
        for operation in range(2):
            if operation:
                karido = -arr[day]+dpNext[0]
                chodo = dpNext[1]
                maxi = max(karido, chodo)
                dpCurr[operation] = maxi
            else:
                becho = arr[day]+dpNext[1]
                chodo = dpNext[0]
                maxi = max(becho, chodo)
                dpCurr[operation] = maxi

        dpNext = dpCurr.copy()
    return dpNext[1]


print(maximumProfit(0, 1))
n = len(arr)
dp = [[-1]*2 for i in range(n)]

print(maximumProfitDP(0, 1, dp))
print(maximumProfitTabDP(arr))
print(maximumProfitTabSpaceOptDP(arr))
