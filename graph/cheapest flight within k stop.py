from typing import List

from collections import defaultdict
from queue import PriorityQueue
class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        
        adj = defaultdict(list)
        
        
        for flightdata in flights:
            start,end,price = flightdata
            
            adj[start].append([end,price])
            
        del flightdata
        pq = PriorityQueue()
        dist = defaultdict(lambda : float("inf"))
        pq.put((0,0,src))
        result = float("inf")
        while not pq.empty():
            stop,price,start = pq.get()
            print(stop,price,start)
            for childdata in adj[start]:
                child,childprice = childdata
                localPrice = childprice+price
                if stop<=k and dist[child]>localPrice:
                    if child==dst:
                        result = min(result,price+childprice)
                    
                    dist[child] = localPrice
                    pq.put((stop+1,localPrice,child))
        
        print(result)       
        return result if result!=float("inf") else -1
                    
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1              
obj = Solution()

obj.CheapestFLight(n,flights,src,dst,k)