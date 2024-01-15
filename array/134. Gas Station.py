from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        
        size = len(gas)
        diff = 0
        total = 0
        index = 0
        for ind in range(size):
            total += gas[ind]-cost[ind]
            if total<0:
                total = 0
                index = ind+1
        return index
    
        
        
obj = Solution()
cost = [3,4,5,1,2]
gas = [1,2,3,4,5]
print(obj.canCompleteCircuit(gas,cost))