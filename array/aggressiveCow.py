#User function Template for python3

#! Url : https://practice.geeksforgeeks.org/problems/aggressive-cows/0


"""
? Time complexity : O(n^2)
? Space complexity : O(1)
"""

def solveBruteForce(k,stalls):
    stalls.sort()
    def checkingCow(mid,k):
        k-=1
        prev = stalls[0]
        for ind,data in enumerate(stalls[1:]):
            if data-prev>=mid:
                prev = data
                k-=1
        return k<=0
        
    low,high = 1,stalls[-1]
    
    ans = 0
    for mid in range(low,high+1):
        if checkingCow(mid,k):
            ans = mid
        else:
            break
        
    return ans


"""
? Time complexity : O(n.log(n))
? Space complexity : O(1)
"""

def solve(k,stalls):
    stalls.sort()
    def checkingCow(mid,k):
        k-=1
        prev = stalls[0]
        for ind,data in enumerate(stalls[1:]):
            if data-prev>=mid:
                prev = data
                k-=1
        return k<=0
        
    low,high = 1,stalls[-1]
    
    ans = 0
    while low<high:
        mid = (low+high)//2
        if checkingCow(mid,k):
            low = mid+1
            ans = mid
        else:
            high = mid
            
    return ans
            
                    
                
                