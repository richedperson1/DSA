
def friendPair(n):
    if n <= 0:
        return 0

    if n <= 2:
        return n

    total = friendPair(n-1)+friendPair(n-2)*(n-1)

    return total


def friendPairDP(n, dp):
    if n <= 0:
        return 0

    if n <= 2:
        return n

    if dp[n] != -1:
        return dp[n]

    total = (friendPairDP(n-1, dp) % 1000000007 +
             (friendPairDP(n-2, dp)*(n-1)) % 1000000007) % 1000000007

    dp[n] = total
    return total


def countFriendsPairings(n):
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2

    for num in range(3, n+1):
        first = dp[num-1] % 1000000007
        second = ((num-1)*dp[num-2]) % 1000000007
        dp[num] = (first+second) % 1000000007

    return dp[-1]


n = 4
# print(friendPair(n)).
dp = [-1]*(n+1)
print(friendPairDP(n, dp))
print(countFriendsPairings(n))
