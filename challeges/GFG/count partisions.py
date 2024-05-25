
from typing import List


class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        # code here
        
        MOD = 10**9 + 7
    
        total_sum = sum(arr)
        
        if (total_sum - d) % 2 != 0 or total_sum < d:
            return 0
        
        target = (total_sum - d) // 2
    
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
                print(dp[j],j,num)
        return dp[target]
    
    
obj = Solution()
n = 4
d = 0
arr =  [1,1,1,1]
print(obj.countPartitions(n,d,arr))