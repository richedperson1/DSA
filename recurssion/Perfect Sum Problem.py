def perfectSum( arr, n, sum):
    dp = [[-1]*(n+1) for ind in range(sum+2)]
    def helper(sumi,ind):
        if ind>=n:
            if sumi==sum:
                return True
            return False
        if dp[sumi][ind]!=-1:
            return dp[sumi][ind]
        if sumi>sum:
            return False
        take = helper(sumi+arr[ind],ind+1)
        NotTake = helper(sumi,ind+1)
        dp[sumi][ind] = take+NotTake
        return take+NotTake
    
    return helper(0,0)

arr = [1, 2, 3, 4, 5]
n = len(arr)
print(perfectSum(arr,n,9))