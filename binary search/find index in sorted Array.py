"""
! URL : https://leetcode.com/problems/find-median-from-data-stream/
"""
arr = [1,2,6,8,9,12]
arr = [2,6,6,10]

size = len(arr)

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if len(self.arr)==0 or self.arr[-1]<num:
            self.arr.append(num)
            return 
        
        elif self.arr[0]>=num:
            self.arr.insert(0,num)
            return 

        else:
            size = len(self.arr)
            low ,high = 0,size-1


            while low<=high:
                mid = (low+high)//2
                
                if self.arr[mid]>=num:
                    high = mid-1
                else:
                    low = mid+1
            self.arr = self.arr[:low]+[num]+self.arr[low:]
        return 
    def findMedian(self) -> float:
        # print(self.arr)
        if not(self.arr):
            return 
        size = len(self.arr)
        if size&1:
            return self.arr[size//2]
        else:
            mid = size//2
            try:
                return (self.arr[mid]+self.arr[mid-1])/2
            except:
                print(self.arr,size)

        


obj = MedianFinder()


new2add =  [[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]

for data in new2add:
    
    if data:
        obj.addNum(data[0])
    else:
        param_2 = obj.findMedian()
        # print(param_2)
        
        
"""
[null,null,6.00000,null,8.00000,null,6.00000,null,6.00000,null,6.00000,null,5.50000,null,6.00000,null,5.50000,null,5.00000,null,4.00000,null,3.00000]

"""