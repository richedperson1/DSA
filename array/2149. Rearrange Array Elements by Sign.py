"""
URL : https://leetcode.com/problems/rearrange-array-elements-by-sign/
"""


"""
Better way to solve this problem

Time complexity : O(n)
Time complexity : O(n)
"""

def rearrangeArray( arr: list[int]) :
    size = len(arr)
    brr = [0]*size
    negInd = size//2
    posInd = 0
    for ind,data in enumerate(arr):
        if data<0:
            brr[negInd] = data
            negInd+=1
        else:
            brr[posInd] = data
            posInd+=1
    negInd = size//2
    posInd = 0
    for i in range(size):
        if i&1==0:
            arr[i] = brr[posInd]
            posInd+=1
        else:
            arr[i]= brr[negInd]
            negInd+=1

    return arr

"""
Optimize way to solve this problem
Time complexity : O(n)
Time complexity : O(n)
"""


def rearrangeArray2( arr: list[int]) :
    size = len(arr)
    brr = [0]*size
    negInd = 1
    posInd = 0
    for ind,data in enumerate(arr):
        if data<0:
            brr[negInd] = data
            negInd+=2
        else:
            brr[posInd] = data
            posInd+=2

    return brr


