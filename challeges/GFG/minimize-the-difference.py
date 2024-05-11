from collections import deque
from typing import List


class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        
        mini = deque([(0,arr[0])])
        maxi = deque([(0,arr[0])])
        
        for ind in range(k):
            
            if mini[-1][-1]>arr[ind]:
                mini.append((ind,arr[ind]))
            
            if maxi[-1][-1]<arr[ind]:
                maxi.append((ind,arr[ind]))
                
        # This part of the code is implementing a sliding window approach to find the minimum difference
        # between the maximum and minimum elements in a subarray of size `k`. Here's a breakdown of what each
        # step is doing:
        
        result = [maxi[-1][-1]-mini[-1][-1]]
        for ind in range(n-k):
            prev = ind
            while mini and mini[0][0]<=prev:
                mini.popleft()
                
            while maxi and maxi[0][0]<=prev:
                maxi.popleft()
                
            local = ind+1
            new = local+k
            while local<new:
                if len(maxi)==0:
                    maxi.append((local,arr[local])) 
                
                elif maxi[-1][-1]<arr[local]:
                    maxi.append((local,arr[local]))
                local+=1
                
            local = ind+1
            while local<new:
                if len(mini)==0:
                    mini.append((local,arr[local])) 
                
                elif mini[-1][-1] > arr[local]:
                    maxi.append((local,arr[local]))
                    
                local+=1
              
            if mini[-1][-1]>arr[ind+k]:
                mini.append((ind+k,arr[ind+k]))
            
            if maxi[-1][-1]<arr[ind+k]:
                maxi.append((ind+k,arr[ind+k])) 
            
            result.append(maxi[-1][-1]-mini[-1][-1])
            
        return result
    
    

obj = Solution()

k = 3
arr = [2, 3, 1, 4, 6, 7]
n = len(arr)


print(obj.minimizeDifference(n,k,arr))
