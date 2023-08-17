"""
URL : https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-115/problems
"""


"""
Time complexity : O(log(n))
Space complexity : O(1)
"""


def completeRows( n : int) -> int:
    # code here
    if n<=0:
        return -1
    if n==1:
        return 1
    
    
    low,high = 1,n
    ans = -1
    while low<=high:
        mid = (low+high)//2
        
        total = (mid*(mid+1))//2
        
        if total>n:
            high = mid-1
        else:
            ans = mid
            low = mid+1
            
    return ans