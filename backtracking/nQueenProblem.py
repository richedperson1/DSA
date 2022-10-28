def printBoard(arr):
    for i in range(len(arr)):
        print(*arr[i])


def canPossibleToPlace(board, i, j):
    # check on the rows
    # print(i, j)
    # return
    row = i
    while row >= 0:
        if board[row][j] == 1:
            return False
        row -= 1

    # check on the left Diagonal

    leftRow = i
    leftCol = j
    while leftRow >= 0 and leftCol >= 0:
        if board[leftRow][leftCol] == 1:
            return False
        leftCol -= 1
        leftRow -= 1

   # check on the Right Diagonal
    n = len(board)
    RightRow = i
    RightCol = j
    while RightRow < n and RightCol < n:
        if board[RightRow][RightCol] == 1:
            return False
        RightCol += 1
        RightRow += 1
    return True


def nQueenPossible(n, board, i):
    if i == n:
        printBoard(board)
        return True

    for j in range(n):
        if canPossibleToPlace(board, i, j):
            board[i][j] = 1
            sucess = nQueenPossible(n, board, i+1)
            if sucess == True:
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
