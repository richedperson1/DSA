
def uniquePath(arr, row, col):
    n = len(arr)-1
    if row == n and col == n:
        return 1

    if row > n or col > n:
        return 0

    if arr[row][col] == 1:
        return 0
    left = uniquePath(arr, row+1, col)
    right = uniquePath(arr, row, col+1)

    return left+right


def uniquePathDP(arr, row, col, dp):
    n = len(arr)-1
    if row == n and col == n:
        return 1

    if row > n or col > n:
        return 0

    9

    if dp[row][col] != -1:
        return dp[row][col]
    left = uniquePathDP(arr, row+1, col, dp)
    right = uniquePathDP(arr, row, col+1, dp)
    dp[row][col] = left+right
    return dp[row][col]


def uniquePathTabDP(arr):
    n = len(arr)-1
    m = len(arr[0])-1
    if arr[n][m] == 1:
        return 0
    n += 1
    m += 1
    dp = [[0]*(m+2) for i in range(n+2)]
    dp[n-1][m-1] = 1

    for row in reversed(range(n)):
        for col in reversed(range(m)):
            if arr[row][col] == 1:
                dp[row][col] = 0

            else:
                down = dp[row+1][col]
                left = dp[row][col+1]
                dp[row][col] = down+left

    return dp[0][0]


arr = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# arr = [[0, 1], [0, 0]]
n = len(arr)
dp = [[-1]*n for i in range(n)]
print(uniquePath(arr, 0, 0))
print(uniquePathDP(arr, 0, 0, dp))
print(uniquePathTabDP(arr))
