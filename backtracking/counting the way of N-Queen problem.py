def printBoard(arr):
    for i in range(len(arr)):
        print(*arr[i])


def canPossibleToPlace(board, i, j):
    # check on the rows
    # print(i, j)
    # return
    for k in range(i):
        if board[k][j] == 1:
            return False

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
        RightRow -= 1

    return True


total = 1


def nQueenPossible(n, board, i):
    # Base case
    if i == n:
        global total

        print(total)
        total += 1
        printBoard(board)
        print("--"*5)
        return 1
    ways = 0
    for j in range(n):
        if canPossibleToPlace(board, i, j):
            board[i][j] = 1
            sucess = nQueenPossible(n, board, i+1)
            ways += sucess
            board[i][j] = 0
    return ways


if __name__ == "__main__":
    n = 5
    board = [[0 for i in range(n)] for i in range(n)]

    ans = nQueenPossible(n, board, 0)
    print(ans)
    pass
