arr = [3, 3, 5, 0, 0, 3, 1, 4]


def stockPrice3(ind, flag, k, dp):
    if k < 0 or ind >= len(arr):
        return 0

    if dp[ind][k][flag] != -1:
        return dp[ind][k][flag]

    if flag:
        kharido = -arr[ind]+stockPrice3(ind+1, 0, k-1, dp)
        bechho = 0+stockPrice3(ind+1, 1, k, dp)
        maxi = max(kharido, bechho)
        dp[ind][k][flag] = maxi
        return maxi
    else:

        kharido = arr[ind]+stockPrice3(ind+1, 1, k, dp)
        bechho = 0+stockPrice3(ind+1, 0, k, dp)
        maxi = max(kharido, bechho)
        dp[ind][k][flag] = maxi
        return maxi


def stockPrice3Tab(arr):
    num = len(arr)
    dp = [[[0]*3 for i in range(3)]for i in range(num+1)]

    for ind in range(num-1, -1, -1):

        for flag in range(2):
            for k in range(1, 3):
                if flag:
                    kharido = -arr[ind]+dp[ind+1][k][0]
                    bechho = dp[ind+1][k][1]
                    # bechho = 0+stockPrice3(ind+1, 1, k, dp)
                    maxi = max(kharido, bechho)
                    dp[ind][k][flag] = maxi
                else:
                    kharido = arr[ind]+dp[ind+1][k-1][1]
                    bechho = 0+dp[ind+1][k][0]
                    maxi = max(kharido, bechho)
                    dp[ind][k][flag] = maxi

    return dp[0][2][1]


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
k = 2
dp = [[[-1]*3 for i in range(3)]for i in range(num+1)]
# print(dp)
print(stockPrice3(0, 2, 2, dp))
print(stockPrice3Tab(arr))
# print(dp)
# print(len(dp))
# print(len(dp[0]))
