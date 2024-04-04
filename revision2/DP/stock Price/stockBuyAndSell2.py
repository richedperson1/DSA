

arr = [3, 3, 4, 2, 5, 8, 0]
dp = [[-1]*(2) for i in range(len(arr)+1)]


def stockPrice(ind, flag):
    if ind >= len(arr):
        return 0

    if flag:
        kharido = -arr[ind]+stockPrice(ind+1, 0)
        rahendo = stockPrice(ind+1, 1)
        ans = max(kharido, rahendo)
        dp[ind][flag] = ans
        return ans

    else:

        kharido = arr[ind]+stockPrice(ind+1, 1)
        rahendo = stockPrice(ind+1, 0)
        ans = max(kharido, rahendo)

        dp[ind][flag] = ans
        return ans


def stockPriceTab(arr):
    n = len(arr)
    dp = [[0]*(2) for i in range(n+1)]

    for ind in range(n-1, -1, -1):
        for flag in range(2):
            if flag:
                kharido = -arr[ind]+dp[ind+1][0]
                rahendo = dp[ind+1][1]
                ans = max(kharido, rahendo)
                dp[ind][flag] = ans
            else:
                kharido = arr[ind]+dp[ind+1][1]
                rahendo = dp[ind+1][0]
                ans = max(kharido, rahendo)
                dp[ind][flag] = ans

    return dp[0][1]


arr = [3, 3, 4, 2, 5, 8, 0]

print(stockPrice(0, 1))
print(stockPriceTab(arr))
