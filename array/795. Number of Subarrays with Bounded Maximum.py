"""
! URL : https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/submissions/
"""

nums = [2,1,4,3] 
left = 2 
right = 3


class Solution:
    totalCount = 0
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) :
        
        high,low = -1,-1
        size = len(nums)
        result = 0
        for ind in range(size):
            if nums[ind]>right:
                high=low = ind
                continue

            if nums[ind]>=left:
                high = ind

            result += (high-low)

        return result

        

obj = Solution()
print(obj.numSubarrayBoundedMax(nums,left,right))