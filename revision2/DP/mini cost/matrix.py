def getMaxGoodLength(A):
    rows = len(A)
    cols = len(A[0])
    max_length = 0

    # Initialize a 2D table to store the lengths of good matrices
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the last row and column of the table
    for i in range(cols):
        dp[rows - 1][i] = 1 if A[rows - 1][i] >= 1 else 0
    for i in range(rows):
        dp[i][cols - 1] = 1 if A[i][cols - 1] >= 1 else 0

    # Fill the remaining cells of the table
    for i in range(rows - 2, -1, -1):
        for j in range(cols - 2, -1, -1):
            if A[i][j] >= 1:
                dp[i][j] = min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1]) + 1

    # Find the maximum length in the table
    for i in range(rows):
        for j in range(cols):
            max_length = max(max_length, dp[i][j])

    return max_length

# Test case
N = 5
M = 4
A = [
    [4, 4, 6, 3],
    [4, 4, 4, 6],
    [3, 5, 5, 5],
    [1, 2, 6, 4],
    [4, 3, 2, 1]
]
A = [[1 ,1 ,1],
     [1 ,1 ,1]]

N = len(A)
M = len(A[0])
result = getMaxGoodLength(A)
print(result)
