"""
URL : https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1
"""
def miniSwap(arr,k):
    miniC = 0
    for ind ,data in enumerate(arr):
        if data<=k:
            miniC+=1
    
    swap = 0
    ans = 0
    for ind ,data in enumerate(arr):
        if miniC>ind:
            if data>k:
                swap+=1
                ans = swap
                
        else:
            if arr[ind-miniC]>k:
                swap-=1
            if arr[ind]>k:
                swap+=1
            
            ans = min(swap,ans)
        
    return ans 


arr = [2,1,5,6,3]
k = 3

n = 20
arr = list(map(int,"4 11 6 5 11 20 19 14 14 2 9 20 11 11 15 1 7 12 19 9".split()))
k = 14
"""20
4 11 6 5 11 20 19 14 14 2 9 20 11 11 15 1 7 12 19 9
14
"""

arr = [1,19,17,2]
k = 1
print(miniSwap(arr,k))