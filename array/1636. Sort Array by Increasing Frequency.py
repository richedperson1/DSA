from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ele_count = Counter(nums)
        # print(ele_count)
        sorted_ele = sorted(nums,key=lambda x:(ele_count[x],-x))
        return(sorted_ele)

    
obj = Solution()
    
nums = [2,2,1,1,2,3]
print(obj.frequencySort(nums))