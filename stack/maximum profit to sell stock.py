import sys
arr = [2, 3, 42, 15, 11,  6]


def maximumProfile(arr):
    n = len(arr)
    stack = [-1]*n
    maxi = arr[-1]
    for ind in range(n-1, -1, -1):
        maxi = max(maxi, arr[ind])
        stack[ind] = maxi

    profit = 0
    mini = sys.maxsize
    for ind in range(n):
        mini = min(mini, arr[ind])

        ans = stack[ind]-mini
        profit = max(profit, ans)

    return profit


print(maximumProfile(arr))
