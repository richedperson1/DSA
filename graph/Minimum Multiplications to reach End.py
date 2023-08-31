"""
! URL : https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
"""

from queue import PriorityQueue
from collections import defaultdict
import sys

def miniMulti2end(arr,start,end):

    dp = [float("inf")]*(end+1)
    def dfs(node):
        if node==end:
            return 0
        
        if dp[node]!=float("inf"):
            return dp[node]
        ans = sys.maxsize

        for data in arr:
            local = (node*data)%(10**5)
            local = dfs(local)+1
            ans = min(local,ans)

        dp[node] = ans
        return ans

    return dfs(start)

def miniMulti2endGraph(arr,start,end):

    total = start

    pq = PriorityQueue()

    pq.put((0,total))

    dist = defaultdict(lambda : float("inf"))
    dist[total] = 0
    while pq.empty()==False:
        step,total = pq.get()

        for mulFact in arr:
            local = total*mulFact
            if local>=(10**5):
                local = local%(10**5)
            if dist[local]>step+1:
                dist[local] = step+1
                pq.put((step+1,local))

        
    return dist[end]

arr = [2, 5, 7]
start = 3 
end = 30




arr = [3, 4, 65]
start,end = 7 ,66175
print(start,end)
print(miniMulti2end(arr,start,end))
print(miniMulti2endGraph(arr,start,end))