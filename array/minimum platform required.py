"""
URL : https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
"""
import heapq
import copy
def minimumPlatform(n,arr,dep):
    arr.sort()
    dep.sort()
    
    size = len(arr)
    a = d = 0
    count = 0
    res = 0
    
    while (a<size and d<size):
        if arr[a]<= dep[d]:
            count+=1
            a+=1
            res = max(count,res)
        else:
            d+=1
            count-=1
            
    return res

arr = [900, 940, 950, 1100, 1500, 1800]
dep = [2300, 1200, 1120, 1130, 1900, 2000]


print(minimumPlatform(len(arr),arr,dep))