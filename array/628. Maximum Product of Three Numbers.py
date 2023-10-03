"""
! URL : https://leetcode.com/problems/maximum-product-of-three-numbers/

"""
from typing import List
import heapq


def maximumProduct( nums: List[int]) -> int:

    ans = heapq.nlargest(3,nums)
    
    small2 = heapq.nsmallest(2,nums)
    larger = heapq.nlargest(1,nums)
    small2.append(larger[0])
    result = 1
    result1= 1
    for data in ans:
        result *= data

    for data in small2:
        result1*=data

    return max(result,result1)