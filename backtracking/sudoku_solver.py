board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


# def isSafe(board, i, j, num):
#     # checking in row top
#     indexR = i
#     indexC = j
#     while indexR >= 0:
#         if board[indexR][indexC] == f"{num}":
#             return False
#         indexR -= 1

#     # checking in row bottom
#     indexBRow = i
#     indexBCol = j
#     while indexBRow < len(board):
#         if board[indexBRow][indexBCol] == f"{num}":
#             return False

#         indexBRow += 1

#     # checking in the column left
#     indexLCol = i
#     indexLRow = j
#     while indexLCol >= 0:
#         if board[indexLRow][indexLCol] == f"{num}":
#             return False
#         indexLCol -= 1

#     # checking in the column Right
#     indexRCol = i
#     indexRRow = j
#     n = len(board)
#     for indexRCol in range(i, n):
#         if board[indexRRow][indexRCol] == f"{num}":
#             return False
#         indexRCol += 1

#     return True


def isSafe(board, i, j, num):

    # checking in row columns
    for k in range(0, 9):
        if board[i][k] == f"{num}" or board[k][j] == f"{num}":
            return False

    startX = (i//3)*3
    startY = (j//3)*3

    for x_axis in range(startX, startX+3):
        for y_axis in range(startY, startY+3):
            if board[x_axis][y_axis] == f"{num}":
                return False
    return True


def sudoku_solver(board, row, col, n):
    if row >= n:
        # print(board)
        return True

    if col == n:
        return sudoku_solver(board, row + 1, 0, n)

    if board[row][col] != ".":
        return sudoku_solver(board, row, col+1, n)

    for num in range(0, 10):
        if isSafe(board, row, col, num):
            board[row][col] = f"{num}"
            flag = sudoku_solver(board, row, col+1, n)
            if flag == True:
                return True

    board[row][col] = "."
    return False


if __name__ == '__main__':
    row = len(board)
    print(row, len(board[0]))
    print(sudoku_solver(board, 0, 0, 9))

    print(board)
