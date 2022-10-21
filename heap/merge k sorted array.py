
import queue
import numpy as np
arr1 = [-2, 3, 4, 5]
arr2 = [5, 6, 7, 8]
arr3 = [15, 16, 27, 88]
arr4 = [51, 61, 71, 88]
arr5 = [2, 5, 6, 7]
arr6 = [3, 5, 7, 8]
arr = [arr1, arr2, arr3, arr4, arr5, arr6]

ans = []


class nodes:
    def __init__(self, data, row, col) -> None:
        self.data = data
        self.row = row
        self.col = col

    def __gt__(self, other):
        if(self.data > other.data):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.data < other.data):
            return True
        else:
            return False

    def __eq__(self, other):
        if(self.data == other.data):
            return True
        else:
            return False


# minQ = queue.PriorityQueue()

# row = len(arr)

# for first in range(row):
#     outPut = nodes(arr[first][0], first, 0)
#     minQ.put(outPut)

# ans = []

# while not(minQ.empty()):
#     mini = minQ.get()
#     ans.append(mini.data)

#     i = mini.row
#     j = mini.col

#     if j+1 < len(arr[i]):
#         newNode = nodes(arr[i][j+1], i, j+1)
#         minQ.put(newNode)


# arr = np.array(arr).reshape(1, -1)[0]
# arr = sorted(arr)
# print(ans == arr)


# Using methods


class nodes_:
    def __init__(self, data: int, row: int, col: int) -> None:
        self.data = data
        self.row = row
        self.col = col

    def __gt__(self, other):
        if(self.data > other.data):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.data < other.data):
            return True
        else:
            return False

    def __eq__(self, other):
        if(self.data == other.data):
            return True
        else:
            return False


def mergeKSortedArrays2(arr, k: int):
    num = len(arr)
    minQ = queue.PriorityQueue()
    for first in range(k):
        outPut = nodes_(arr[first][0], first, 0)
        minQ.put(outPut)

    ans = []
    while not(minQ.empty()):
        mini = minQ.get()
        ans.append(mini.data)

        i = mini.row
        j = mini.col

        if j+1 < len(arr[i]):
            newNode = nodes_(arr[i][j+1], i, j+1)
            minQ.put(newNode)
            j += 1
    return(ans)


def mergeKSortedArrays(arr, k: int):
    num = len(arr)
    minQ = queue.PriorityQueue()
    for first in range(k):
        outPut = nodes_(arr[first][0], first, 0)
        minQ.put(outPut)

    ans = []
    while not(minQ.empty()):
        mini = minQ.get()
        ans.append(mini.data)

        i = mini.row
        j = mini.col

        if j+1 < len(arr[i]):
            newNode = nodes_(arr[i][j+1], i, j+1)
            minQ.put(newNode)
            j += 1
    return(ans)


print(mergeKSortedArrays(arr, len(arr)))
# nodes_(5, 6, 7)
