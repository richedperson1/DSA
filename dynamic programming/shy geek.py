"""
Contest coding quection
"""

import sys
sys.setrecursionlimit(10**8)


def shyGeek(arr, k):
    if k < 0:
        return sys.maxsize
    if k == 0:
        return 0

    ans = sys.maxsize

    for data in arr:
        newK = k-data
        if newK >= 0:
            local = shyGeek(arr, newK)+1
            ans = min(local, ans)

    return ans


def shyGeekDP(arr, k, n, dp):
    if k < 0:
        return sys.maxsize
    if k == 0:
        return 0

    if dp[k] != -1:
        return dp[k]
    ans = sys.maxsize

    for ind in range(n-1, -1, -1):
        data = arr[ind]
        newK = k-data
        if newK >= 0:
            local = shyGeekDP(arr, newK, n, dp)+1
            ans = min(local, ans)
    dp[k] = ans
    return ans


def shyGeekDP_tab(arr, n, k):
    dp = [0]*(k+1)

    for price in range(1, k+1):
        ans = 1 if min(arr) <= k else sys.maxsize
        for ind in range(n-1, -1, -1):
            data = arr[ind]
            newK = price-data
            if newK >= 0:
                local = dp[newK]+1
                ans = min(local, ans)

        dp[price] = ans

    return dp[-1]


arr = [2, 4, 6, 8][::-1]
arr = [1, 2, 2, 4]
arr = list(map(int, "6 6 10 13 27 32 32 36 47 54 55 57 57 60 62 63 63 67 70 70 70 72 72 74 77 82 82 82 90 91 92 101 101 101 104 113 115 117 121 121 123 126 126 126 127 127 129 132 135 137 140 141 142 145 150 151 155".split()))
print(len(arr))

k = 7

# print(shyGeek(arr, k))
dp = [-1]*(k+1)
n = len(arr)
print(shyGeekDP(arr, k, n, dp))
print(shyGeekDP_tab(arr, n, k))
