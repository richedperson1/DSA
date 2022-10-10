from heapClass import *


class heapSort(heap):
    def sorting(self):
        print(">>>>>>>", self.storage, "<<<<<<<<")
        while self.size > 1:
            self.swap(1, self.size)
            self.size -= 1
            self.hepifyRule(1)
        return self.storage

    def hepifyRule(self, index):
        largest = index

        while largest < self.size:
            leftS = 2*index
            rightS = 2*index+1
            if leftS <= self.size and self.storage[leftS] > self.storage[largest]:
                largest = leftS
            if rightS <= self.size and self.storage[rightS] > self.storage[largest]:
                largest = rightS
            # break
            if index != largest:
                self.swap(index, largest)
                index = largest
            else:
                return


heapi = heapSort()
heapi.insert(14)
heapi.insert(13)
heapi.insert(10)
heapi.insert(-12)
heapi.insert(1+8)
heapi.insert(-90)
heapi.insert(90)
print(heapi.sorting())
