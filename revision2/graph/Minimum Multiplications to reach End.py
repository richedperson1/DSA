#User function Template for python3

from typing import List
from collections import deque,defaultdict
import sys
sys.setrecursionlimit(10**8)
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        dq = deque([(0,start)])
        
        dist = [float("inf")]*100009
        while len(dq)>0:
            step,node = dq.popleft()
            if node==end:
                return step
            
            
            for multi_factor in arr:
                local = (node*multi_factor)%100000
                if dist[local]>step+1:
                    dist[local] = step+1
                    dq.append((step+1,local))
        
        return -1
    def minimumMultiplications2(self, arr : List[int], start : int, end : int) -> int:
        
        visit = defaultdict(int)
        dp = defaultdict(lambda : float("inf"))
        def dp_code(start,end):
            
            if start==end:
                return 0
                
            if start>end or start in visit:
                return float("inf")
                
            if dp[start]<float("inf"):
                return dp[start]
            
            result = float("inf")
            for child in arr:
                local = (start*child)%100000
                if local>end:
                    continue
                
                if local in visit:
                    return dp[local]
                result = min(result,dp_code(local,end))
                visit[local] = 1
            dp[start] = result+1
            return dp[start]
            
        if dp_code(start,end)>=float("inf"):
            return -1
        return dp[start]
    
arr= [2, 5]
start = 3
end = 306

arr= [3, 4, 65]
start = 7
end = 66175 
print(Solution().minimumMultiplications2(arr,start,end))

# print(end%100000)
