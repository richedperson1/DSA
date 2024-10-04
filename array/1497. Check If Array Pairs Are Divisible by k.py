from collections import defaultdict
from typing import List
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dist = defaultdict(set)

        for ind,data in enumerate(arr):
            mod_data = data%k
            dist[mod_data].add(ind)
        # print(dist)
        for ind,data in enumerate(arr):

            moding = data%k
            remain = k-moding
            print(remain)
            if remain in dist and not(ind in dist[remain]):
                return True
        return False
    

obj = Solution()

arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
arr = [1,2,3,4,5,6]
k = 10
print(obj.canArrange(arr,k))