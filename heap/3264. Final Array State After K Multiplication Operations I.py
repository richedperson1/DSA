import heapq
from typing import List
from queue import PriorityQueue

class Solution:
    def getFinalState(self, arr: List[int], k: int, multiplier: int) -> List[int]:
        customers = PriorityQueue() 
        
        for ind,data in enumerate(arr):
            customers.put((data,ind))
            
            
        for ind in range(k):
            if not customers.empty():
                ele,index = customers.get()
                arr[index] = ele*multiplier
                customers.put((arr[index],index))
        return arr
        


arr = [2,1,3,5,6]

obj = Solution()
multiplier,k = 2,5
print(obj.getFinalState(arr,k,multiplier))