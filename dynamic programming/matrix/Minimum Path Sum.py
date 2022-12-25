import sys


def miniPathSum(arr, indI, indJ, n, m):
    if indI >= n-1 and indJ >= m-1:
        return arr[indI][indJ]
    if indI >= n or indJ >= m:
        return sys.maxsize

    right = miniPathSum(arr, indI, indJ+1, n, m)+arr[indI][indJ]
    down = miniPathSum(arr, indI+1, indJ, n, m)+arr[indI][indJ]

    return min(right, down)


def miniPathSumDP(arr, indI, indJ, n, m, dp):
    if indI >= n-1 and indJ >= m-1:
        return arr[indI][indJ]
    if indI >= n or indJ >= m:
        return sys.maxsize

    if dp[indI][indJ] != -1:
        return dp[indI][indJ]
    right = miniPathSumDP(arr, indI, indJ+1, n, m, dp)+arr[indI][indJ]
    down = miniPathSumDP(arr, indI+1, indJ, n, m, dp)+arr[indI][indJ]

    ans = min(right, down)

    dp[indI][indJ] = ans
    return ans


def miniPathTabDP(arr):
    n, m = len(arr), len(arr[0])
    dp = [[sys.maxsize]*(m+1) for j in range(n+1)]
    indI = n-1
    indJ = m-1
    dp[indI+1][indJ] = 0
    dp[indI][indJ+1] = 0
    for row in range(indI, -1, -1):
        for col in range(indJ, -1, -1):
            right = dp[row][col+1]+arr[row][col]
            down = dp[row+1][col]+arr[row][col]

            ans = min(right, down)
            dp[row][col] = ans

    return dp[0][0]


def miniPathTabDP_Opt(arr):
    n, m = len(arr), len(arr[0])
    dp = [[sys.maxsize]*(m+1) for j in range(n+1)]
    indI = n-1
    indJ = m-1

    currDP = [sys.maxsize]*(m+1)
    nextDP = [sys.maxsize]*(m+1)
    currDP[indI+1] = 0
    nextDP[indJ+1] = 0
    for row in range(indI, -1, -1):
        for col in range(indJ, -1, -1):
            right = currDP[row+1]+arr[row][col]
            down = nextDP[col]+arr[row][col]

            ans = min(right, down)
            currDP[row] = ans
        nextDP = currDP.copy()
        currDP = [sys.maxsize]*(m+1)
        currDP[-1] = 0
    return currDP


grid = [[1, 2, 3], [4, 5, 6]]

n, m = len(grid), len(grid[0])

print(miniPathSum(grid, 0, 0, n, m))
dp = [[-1]*m for j in range(n)]
print(miniPathSumDP(grid, 0, 0, n, m, dp))

print(miniPathTabDP(grid))
print(miniPathTabDP_Opt(grid))
