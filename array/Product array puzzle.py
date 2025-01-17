class Solution:
    def productExceptSelf(self, arr):
        #code here
        
        local = 1
        size = len(arr)
        left = []
        prev = 1
        for ind in reversed(range(size)):
            prev *= arr[ind]
            left.append(prev)
        left = left[::-1]
        first = arr[0]
        results = [left[1]]
        for ind in range(1,size-1):
            local = left[size-ind-1]*first
            
            first *= arr[ind]
            results.append(local)
        
        results.append(first)
        return results
    

obj = Solution()
arr = [1,0,2,12]

print(obj.productExceptSelf(arr))