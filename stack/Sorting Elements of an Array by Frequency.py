# 4 6 9 19 2 16 13 11 16 17 16 8 12 16 12 18

from collections import Counter
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        dist = Counter(arr)
        
        result = sorted(dist.items(),key = lambda x: (-x[1],x[0]))
        final = []
        for key,val in result:
            for _ in range(val):
                final[ind] = key
                
        return final
    
obj =  Solution()


arr = list(map(int,"4 6 9 19 2 16 13 11 16 17 16 8 12 16 12 18".split()))
print(obj.sortByFreq(arr))