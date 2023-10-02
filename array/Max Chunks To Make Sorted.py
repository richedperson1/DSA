
"""
! URL : https://leetcode.com/problems/max-chunks-to-make-sorted/
"""

"""
Time complexity : O(n)
Space complexity : O(1)
"""
def maxChunks(arr):
    max_so_far = arr[0]
    
    count = 0
    
    for i in range(len(arr)):
        if max_so_far<arr[i]:
            max_so_far = arr[i]
            
        if max_so_far == i:
            count+=1
            
    return count

