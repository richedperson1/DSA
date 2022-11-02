def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    if nStairs == 1:
        return 1
    first = 1
    second = 2
    for num in range(3, nStairs+1):
        third = first+second
        first = second
        second = third
    return second


# print(countDistinctWays(51))


def countHelper(n, dp):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if dp[n] != 0:
        return dp[n]
    dp[n] = countHelper(n-1, dp)+countHelper(n-2, dp)
    return dp[n]


def countDistinctWays2(nStairs: int) -> int:
    #  Write your code here.
    dp = [0]*(nStairs+1)
    return countHelper(nStairs, dp)


print(countDistinctWays2(49))
