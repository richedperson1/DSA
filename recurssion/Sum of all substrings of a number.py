class Solution:
    #Function to find sum of all possible substrings of the given string.
    def sumSubstrings(self,s):
        
        # code here
        n = len(s)
        dp = [0]*n
        dp[0] = int(s[0])
        for ind in range(1,n):
            local = dp[ind-1]*10+int(s[ind])
            dp[ind] = local+int(s[ind])+dp[ind-1]

        return dp[ind]


print(Solution().sumSubstrings("1234"))