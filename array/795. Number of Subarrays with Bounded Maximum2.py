

nums = [2,3,4,3] 
left = 2 
right = 4


class Solution:
    totalCount = 0
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) :
        
        high,low = -1,-1
        size = len(nums)
        result = 0
        local = []
        ans = []
        for ind in range(size):
            if nums[ind]>right or nums[ind]< left:
                high=low = ind
                local = []
                continue

            if nums[ind]>=left:
                local.append(nums[ind])
                high = ind

            ans.append(local)
            result += (high-low)
        print(ans)
        return result

        

obj = Solution()
print(obj.numSubarrayBoundedMax(nums,left,right))