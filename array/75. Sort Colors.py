"""
URL : https://leetcode.com/problems/sort-colors/
"""


arr = [2,0,2,1,1,0]

"""
Time complexity : O(n.log(n))
Time complexity : O(1)
"""
def bruteForce():
    return sorted(arr)


"""
Time complexity : O(n)
Time complexity : O(1)
"""

def optimalApproach():
    zero = 0
    two = len(arr)-1
    mid = 0

    while(zero<two and mid<=two):
        if arr[mid]==0:
            arr[mid],arr[zero] = arr[zero],arr[mid]
            zero+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        
        else:
            arr[mid],arr[two] = arr[two],arr[mid]
            two-=1

    return arr



print(optimalApproach())