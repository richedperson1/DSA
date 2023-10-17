"""
! URL : https://leetcode.com/problems/maximum-product-subarray/
"""

def maxiPro(arr):
    total = 1
    maxi = -float("inf")
    mini = float("inf")
    for ind,data in enumerate(arr):
        if data==0:
            total = max(total,0)
            maxi,mini = 0,0

        temp = maxi*data

        maxi = max(maxi*data,mini*data,data)
        mini = min(temp,mini*data,data)
        total = max(total,maxi)
    return total



arr = [3,-1,4,-2]
arr = [2,3,-2,4]
arr = [-2,0,-1]

maxiPro(arr)