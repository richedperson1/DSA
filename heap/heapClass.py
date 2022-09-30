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
