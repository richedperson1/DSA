class Solution:
    def findMaxDiff(self, arr):
        
        left = [0]
        right = [0]
        size = len(arr)
        rv = arr[-1]
        lv = arr[0]
        for ind in range(1,size):
            if arr[ind]>lv:
                left.append(lv)
                lv = arr[ind]
            else:
                left.append(0)
                lv = arr[ind]
            
            if arr[-(ind+1)]>rv:
                right.append(rv)
                rv = arr[-(ind+1)]
            else:
                right.append(0)
                rv = arr[-(ind+1)]

        
        result = 0
        right = right[::-1]
        print(left,right)
        # return [1,2,3]
        for ind,data in enumerate(left):
            result = max(abs(left[ind]-right[ind]),result)
        
        return result
                
obj  = Solution()

arr = [1,2,3,4,5,6,7,8]
print(obj.findMaxDiff(arr))