"""
URL : https://practice.geeksforgeeks.org/problems/longest-arithmetic-progression1019/1
"""

arr = [1, 7, 10, 13, 14, 19]


def checkingLAP(arr, ind, local):
    if ind >= len(arr):
        return 0

    ans = 0
    if local[-1] != 0:
        local[-1] = arr[ind]
        inc = checkingLAP(arr, ind+1, local)+1
        local[-1] = arr[ind]
        exc = 0
    return ans
