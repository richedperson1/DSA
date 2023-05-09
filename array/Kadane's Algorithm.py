"""
Love Babbar DSA sheet

URL : https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
"""

import sys

"""
The function finds the maximum sum of a continuous subarray in a given array using a nested loop.

:param arr: an input list of integers
:return: The function `maximumContinuous` returns the maximum sum of a continuous subarray in the
input array `arr`.
"""
 
"""
Time complexity : O(n^2)
Space complexity : O(1)
"""
def maximumContinuous(arr):
    final = -sys.maxsize

    size = len(arr)
    for ind in range(size):
        total = 0
        for ind2 in range(ind,size):
            total+=arr[ind2]
            final = max(final,total)

    return final


        
"""
Time complexity : O(n)
Space complexity : O(1)
"""

def maximumContinuous1(arr):
    final = -sys.maxsize

    size = len(arr)
    total = final
    # print(arr)
    for ind in range(size):

        if total+arr[ind] < arr[ind]:
            total = arr[ind]
            final = max(total,final)
        else:
            total+=arr[ind]
            final = max(total,final)
    return final

"""
Modified above one
"""

"""
The function `maximumContinuous2` returns the maximum sum of a continuous subarray in a given array.

:param arr: The input array of integers for which we need to find the maximum sum of a continuous
subarray
:return: The function `maximumContinuous2` is returning the maximum sum of a contiguous subarray in
the input array `arr`.

"""
def maximumContinuous2(arr):
    final = -sys.maxsize

    size = len(arr)
    total = final
    # print(arr)
    for ind in range(size):
        
        total = max(total+arr[ind],arr[ind])
        final = max(total,final)
        pass
    return final


# Edge case only
arr = [-5, -2, -6, -8, -1]
arr = [2, 5, 1, 7, 3]
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
arr = [0]*5
arr = [5]

print(maximumContinuous1(arr))
print(maximumContinuous2(arr))