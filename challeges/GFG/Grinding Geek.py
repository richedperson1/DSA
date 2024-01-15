from typing import List
import math

class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        dp = {}
        def max_product(ind,total):
            if total<=0:
                if total==0:
                    return 0
                return -1
            if ind>=len(cost):
                return 0
            
            if dp.get((total,ind),False)!=False:
                return dp.get((total,ind))
            data = cost[ind]
            new_total = math.floor(total-(10/100*cost[ind]))
            pickup = 0
            if cost[ind]<=total:
                pickup = max_product(ind+1,new_total)+1
            not_pickup = max_product(ind+1,total)
            dp[(total,ind)] = max(pickup,not_pickup)
            return dp[(total,ind)]
        
        # new_arr = []
        # num = 0
        # for ind,data in enumerate(cost):
        #     if data<=total :
        #         new_arr.append(data)
        
        # cost = new_arr
        return max_product(0,total)


arr = [10,1,1,1,1,1,1,1,1,9,1,1]

k = 10
# arr,k = [18, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 18
n = len(arr)
obj = Solution()



# 7
# 19
# 2 35 97 16 87 26 62

arr = list(map(int,"2 35 97 16 87 26 62".split()))
k = 19
n = len(arr)

print(obj.max_courses(n,k,arr))