class Solution:
    def maxPoints(self, arr: List[List[int]]) -> int:
        # This code snippet is implementing a dynamic programming solution to solve a problem. Here's a
        # breakdown of what the code is doing:
        
        

        rows ,cols = len(arr),len(arr[0])

        dp = arr[0]
        for ind in range(1,rows):
            left = [0]*cols
            right= [0]*cols

            left[0] = dp[0]

            for l_ind in range(1,cols):
                left[l_ind] = max(left[l_ind-1]-1,dp[l_ind])

            
            right[-1] = dp[-1]
            dp[-1] = left[-1]+arr[ind][-1]
            for r_ind in range(cols-2,-1,-1):
                right[r_ind] = max(right[r_ind+1]-1,dp[r_ind])

                dp[r_ind] = max(left[r_ind],right[r_ind])+arr[ind][r_ind]

            # for d_ind in range(cols):
                # dp[d_ind] = max(left[d_ind],right[d_ind])+arr[ind][d_ind]

        return max(dp)