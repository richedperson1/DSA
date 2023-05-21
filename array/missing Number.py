"""
URL : https://leetcode.com/problems/missing-number
"""

"""
Time complexity : O(n)
Space complexity : O(n)
"""
def missingNumber( arr: list[int]) -> int:
    
    dist = {}
    for ind,data in enumerate(arr):
        dist[data] = ind

    num = len(arr)
    for ind in range(num+1):
        if dist.get(ind,-1)==-1:
            return ind
    return False


"""
Time complexity : O(n)
Space complexity : O(1)
"""
def missingNumber2( arr: list[int]) -> int:
    
    sumi = sum(arr)

    n = len(arr)
    total = ((n+1)*n)//2

    return sumi-total