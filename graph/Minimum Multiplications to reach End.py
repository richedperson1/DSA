"""
! URL : https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
"""


arr = [2, 5, 7]
start = 3 
end = 30

import sys
def miniMulti2end(arr,start,end):

    dp = [float("inf")]*(end+1)
    def dfs(node):
        if node==end:
            return 0
        
        if node>end:
            return sys.maxsize
        
        if dp[node]!=float("inf"):
            return dp[node]
        ans = sys.maxsize

        for data in arr:
            local = dfs(node*data)+1
            ans = min(local,ans)

        dp[node] = ans
        return ans

    return dfs(start)

print(miniMulti2end(arr,start,end))