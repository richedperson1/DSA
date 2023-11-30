
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def minimumStep (self, n):
    
        dp = {}
        def dpProblem(ind):
        
            if ind==n:
                return 0
            if ind>n:
                return float("inf")
            
            if ind in dp:
            
                return dp[ind]
            
            ans1 = dpProblem(ind+1)
            ans2 = dpProblem(3*ind)
            
            ans = min(ans1,ans2)+1
            dp[ind] = ans
            return ans
        
        return dpProblem(1)
    

obj = Solution()
print(obj.minimumStep(99617))