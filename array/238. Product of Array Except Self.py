"""
URL : https://leetcode.com/problems/product-of-array-except-self/
"""


def productExceptSelf( arr: list[int]) -> list[int]:
    size = len(arr)
    total = 1
    final = [0]*(size+1)
    final[-1] = 1
    for ind in reversed(range(size)):
        total*=arr[ind]
        final[ind] = total

    total = 1

    for j in range(size):
        final[j] = total*final[j+1]
        total*=arr[j]
    
    return final[:-1]




def productExceptSelfSinglePass(arr):
    pre = 1
    post= 1
    num = len(arr)
    final = [1]*num

    for ind in range(num):
        final[ind] *= pre
        pre *= arr[ind]

        final[num-ind-1] *= post

        post *= arr[num-ind-1]

    return final