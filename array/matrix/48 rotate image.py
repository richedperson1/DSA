import numpy as np


grid = [ind for ind in range(1,26)]

grid = np.array(grid).reshape(-1,int(len(grid)**0.5))
def rotateImg(grid):
    # The code you provided is a function called `rotateImg` that takes a 2D grid as input and rotates it
    # in a clockwise direction.

    rowEnd = len(grid)-1

    rowStart = 0
    while rowStart<=rowEnd:
        
        for index in range(rowStart,rowEnd):
            temp = grid[rowStart][index]
            current2 = grid[index][rowEnd]
            grid[index][rowEnd] = temp
            temp = current2

            current3 = grid[rowEnd][-(index+1)]
            grid[rowEnd][-(index+1)] = temp
            temp = current3

            current4 = grid[-(index+1)][rowStart]
            grid[-(index+1)][rowStart]= temp
            temp = current4

            grid[rowStart][index] = temp
            print(grid)
            print("--"*5)


            
            
        rowStart+=1
        rowEnd-=1
    print("final output")
    print(grid)

rotateImg(grid)

for data in grid:
    print(list(data),end=",")