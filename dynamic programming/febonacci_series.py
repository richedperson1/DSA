
# with simple recursion solution
count = 0

n = 15


def feboSimple(n):
    if n <= 2:
        return 1
    return feboSimple(n-1)+feboSimple(n-2)


# with DP solution
count1 = 0


def feboDP(n):
    if n <= 2:
        return 1

    if arr[n] != 0:
        return arr[n]

    arr[n] = feboDP(n-1)+feboDP(n-2)
    return arr[n]


arr = [0]*(n+1)


def nthFibonacci(num):
    dp = [1]*3
    for n in range(3, num):
        local = dp[n-1]+dp[n-2]
        dp.append(local)

    return dp[-1]

# Febo series using varible


def feboTabular(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    temp = 0
    for num in range(2, n):
        temp = first+second
        first = second
        second = temp

    return temp


n = 4
print(nthFibonacci(n))
print(feboTabular(n))
# print("\nWith DP Tabular format is answer ")
# print(f"{n}th febo series is : ", feboTabular(n))
# print("Number of recursion call is : ", n)
