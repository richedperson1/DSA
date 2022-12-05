def nthStair(num):
    dp = [1]
    for n in range(1, num+1):
        local = 1
        if n-2 >= 0:
            local = dp[n-2]+1
            dp.append(local)
        else:
            dp.append(local)

    return dp


num = 4
print(nthStair(num))
