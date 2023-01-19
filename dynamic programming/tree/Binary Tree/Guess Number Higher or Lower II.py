"""
URL : https://leetcode.com/problems/guess-number-higher-or-lower-ii/submissions/880966915/
"""

n = 10


def guessNumber(i, n):
    if i >= n:
        return 0

    ans = float("inf")

    for start in range(i, n):
        ans = min(ans, start+max(guessNumber(i, start-1),
                  guessNumber(start+1, n)))

    return ans


def guessNumberDP(start, end, dp):
    if start >= end:
        return 0

    if dp[start][end] != -1:
        return dp[start][end]

    ans = float("inf")
    for i in range(start, end):
        ans = min(ans, i+max(guessNumberDP(start, i-1, dp),
                  guessNumberDP(i+1, end, dp)))

    dp[start][end] = ans
    return ans


def guessNumberTabDP(end):
    n = end
    dp = [[0]*(n+1)for i in range(n+2)]

    for start in range(n, 0, -1):
        for end in range(start, n+1):
            if start == end:
                continue
            else:
                ans = float('inf')
                for ii in range(start, end+1):
                    ans = min(ans, ii+max(dp[start][ii-1], dp[ii+1][end]))

                dp[start][end] = ans

    return dp[1][n]


print(guessNumber(1, n))
dp = [[-1]*(n+1)for i in range(n+1)]

print(guessNumberDP(1, n, dp))
print(guessNumberTabDP(n))
