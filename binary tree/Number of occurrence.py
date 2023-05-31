"""
URL : https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
"""

arr = list(map(int,"1 1 2 2 2 2 3".split()))
tar = 4


#User function Template for python3
def seachLow(arr,tar):
    low,high = 0,len(arr)-1
    
    ans = -2
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==tar:
            ans = mid
            high = mid-1
        elif arr[mid]>tar:
            high = mid-1
        else:
            low = mid+1
    return ans
    
def seachHigh(arr,tar):
    
    low,high = 0,len(arr)-1
    ans = -4
    
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==tar:
            ans = mid
            low = mid+1
        elif arr[mid]>tar:
            high = mid-1
        else:
            low = mid+1
    return ans



print(seachHigh(arr,tar)-seachLow(arr,tar))