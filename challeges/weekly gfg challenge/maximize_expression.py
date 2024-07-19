from typing import List
class Solution:
    def maximiseExpression(self, n : int, arr : List[int]) -> int:
        # code here
        mini = min(arr)
        
        first = 0
        second= 0
        
        for data in arr:
            if data>first:
                second = first
                first = data
                
            elif data>second :
                second = data
                
           
        
        # print(first,second,mini)
        return (first+second)-mini
        
        
obj = Solution()
n = 3
arr = list(map(int,"36 20 26 37 3 8 17 10 37 6 25 33 33 8 15 21 28 36 8 15 28 33 50 34 36 50 4 19 39 30 24 27 47 29 48 26".split()))
arr.sort(reverse=True)
print(len(arr))
print(obj.maximiseExpression(n,arr))
