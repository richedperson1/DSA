"""
! URL : https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-118/problems
"""
from typing import *

arr = [2, 1, 1, 2, 1, 2, 2]
C = 1

def maxBoxes( N : int, C : int, col : List[int]):
    if N<3:
        return 0
    
    sameColorIdx = []
    count = 0
    for ind,color in enumerate(col):
        
        if color==C:
            count+=1
            if count==2:
                sameColorIdx.append(ind+1)
        else:
            count = 0
            
    
    ans = 0
    for ind in sameColorIdx:
        newArr = col[:ind-2]  +col[ind:]
        total = 2
        
        # for ind in range(len(newArr)-1):


            
        ans = max(ans,total)
    return ans


arr = [2, 1, 1,2, 1, 2, 2]
# arr = [1,1,2,2,1]
C = 1

print(maxBoxes(len(arr),C,arr))