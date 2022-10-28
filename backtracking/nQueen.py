def printBoard(arr):
    for i in range(len(arr)):
        print(*arr[i])


def isSafe(board, row, col):
    # checking in row
    indexR = row
    indexC = col
    while indexR >= 0:
        if board[indexR][indexC] == 1:
            return False

        indexR -= 1

    # checking in the column
    while indexC >= 0:
        if board[indexR][indexC]:
            return False

        indexC -= 1

    # checking in the left diagonal
    leftRow = row
    leftCol = col
    while leftRow >= 0 and leftCol >= 0:
        if board[leftRow][leftCol]:
            return False
        leftCol -= 1
        leftRow -= 1

    # checking in the right diagonal
    rightCol = col
    rightRow = row
    while rightRow >= 0 and rightCol < n:
        if board[rightRow][rightCol]:
            return False

        rightCol += 1
        rightRow -= 1

    return True


def nQueenPossible(n, board, i):
    if i >= n:
        printBoard(board)
        return True

    for j in range(n):
        if isSafe(board, i, j):
            board[i][j] = 1
            final = nQueenPossible(n, board, i+1)
            if final:
                return True
            board[i][j] = 0

    return False


if __name__ == "__main__":
    quen = 5
    n = 5
    board = [[0 for i in range(n)] for i in range(n)]

    ans = nQueenPossible(quen, board, 0)
    print(ans)
    pass
