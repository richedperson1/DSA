class heap:
    def __init__(self):
        self.storage = [0]
        self.size = 0

    def insert(self, val):
        self.size += 1
        index = self.size
        self.storage.append(val)

        while index > 1:
            parent = index//2
            if self.storage[parent] < self.storage[index]:
                temp = self.storage[parent]
                self.storage[parent] = self.storage[index]
                self.storage[index] = temp
                index = parent
            else:
                return

    def printingHeap(self):
        for ind, num in enumerate(self.storage):
            if ind == 0:
                continue
            print(num, end=" ")

    def delete(self):
        if self.size <= 1:
            return "Deletion of operation not possible"

        self.size -= 1

        self.storage[1] = self.storage[-1]
        self.storage.pop()
        self.deleteHelper(1)
        return self.storage[1:]

    def deleteHelper(self, index):
        if index > self.size:
            return self.storage

        rightIndex = 2*index+1
        leftIndex = 2*index
        if leftIndex <= self.size and self.storage[index] < self.storage[leftIndex]:
            self.swap(leftIndex, index)
            return self.deleteHelper(leftIndex)
        elif rightIndex <= self.size and self.storage[index] < self.storage[rightIndex]:
            self.swap(rightIndex, index)
            return self.deleteHelper(rightIndex)
        return self.storage

    def swap(self, a, b):
        self.storage[a], self.storage[b] = self.storage[b], self.storage[a]

    def sortArray(self):
        i = 1
        arr = [0]*self.size
        while self.size >= 1:
            self.swap(a=1, b=self.size)
            arr[self.size-1] = self.storage[self.size]
            self.sortHelper(1)
            i += 1
            self.size -= 1
        return self.storage

    def sortHelper(self, index):
        largest = index
        leftSide = 2*index
        rightSide = 2*index+1
        if leftSide < self.size and self.storage[leftSide] > self.storage[index]:
            index = leftSide
        if rightSide < self.size and self.storage[rightSide] > self.storage[index]:
            index = rightSide

        if largest != index:
            self.swap(index, largest)
            self.sortHelper(largest)

    def hepify(self, arr, index, size):
        largest = index
        leftSide = index*2
        rgtSide = index*2+1

        if leftSide < size and arr[largest] < arr[leftSide]:
            largest = leftSide
        if rgtSide < size and arr[largest] < arr[rgtSide]:
            largest = rgtSide

        if largest != index:
            arr[largest], arr[index] = arr[index], arr[largest]
            self.hepify(arr, largest, size)
