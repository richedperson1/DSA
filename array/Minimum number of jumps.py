"""
URL : https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
"""
import sys

def miniJumps(arr,ind):
    size = len(arr)
    if ind>=size-1:
        return 0
    if arr[ind]==0:
        return sys.maxsize
    
    start = ind
    end = ind+arr[ind]
    final = sys.maxsize
    for ind2 in range(start,end):
        final = min(final,miniJumps(arr,ind2+1))+1
    return final

def miniJumpRecursion(arr):
    size = len(arr)
    if size<=1:
        return 0
    if arr[0]==0:
        return -1
    
    return miniJumps(arr,0)

"""
Optimize solution 

T.C = O(n)
S.C = O(1)
"""

def miniJump(arr):
    if len(arr)<=1:
        return 0
    if arr[0]==0:
        return  -1
    
    step = arr[0]
    maxReach = step
    size = len(arr)
    jump = 1
    for ind in range(1,size):
        if ind==size-1:
            return jump
        
        maxReach = max(maxReach,ind+arr[ind])
        # if maxReach<=size-1:
        #     return jump
        
        step-=1
        if step==0:
            jump+=1
            if ind>=maxReach:
                return -1
            
            step = maxReach-ind
        


arr = [[0],[1,2,3],[3],[5,4,3,2,1],[654,81,81,98,84,84,987,81,654,98,6],[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],[1, 4, 3, 2, 6, 7],
       [3,2,2,1,4,5],[2,0,0,3],[1,0,0,0],[2,0,0]]


for subArr in arr:
    first = miniJump(subArr)
    second = miniJumpRecursion(subArr)
    print(first,second)