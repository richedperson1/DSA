"""
URL : https://practice.geeksforgeeks.org/problems/rotation4723/1
"""


def rotateFind(arr):
    n = len(arr)
    low,high = 0,n-1
    while low<high:
        mid = (low+high)//2
        
        nxt = (mid+1)%n
        prev= (mid-1)%n
        if arr[nxt]<arr[mid]>arr[prev] :
            return mid+1
            
        if arr[mid]>arr[0]:
            low = mid+1
        else:
            high = mid
    
    return 0


arr = [4,6]
print(rotateFind(arr))