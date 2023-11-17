import math

"""
! URL : https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""

def smallestDivisor( nums: list[int], threshold: int) :
    if len(nums)>threshold:
        return -1
    def isPossible(arr,thre,mid):

        local = 0
        for data in arr:
            division = math.ceil(data/mid)
            local += division

            if local>thre:
                return False

        return True


    low,high = 1,max(nums)
    ans = float("inf")
    while low<=high:
        mid = (low+high)//2
        if isPossible(nums,threshold,mid):
            ans = min(ans,mid)
            high = mid-1
        else:
            low = mid+1

    return ans
