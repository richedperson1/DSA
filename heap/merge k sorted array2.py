import queue
import heapq

arr1 = [2, 3, 4, 5]
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


minQ = queue.PriorityQueue()

row = len(arr)

for first in range(row):
    minQ.put(arr[first][0])

ans = []
i = 0
j = 1
while not(minQ.empty()):
    mini = minQ.get()
    ans.append(mini)

    while j+1 < len(arr[i]):
        minQ.put(arr[i][j+1])
        j += 1
    i += 1

print(ans)
