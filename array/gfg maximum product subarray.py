class Solution:
    def maxProduct(self,arr,n):
        result = 1
        maxi = -float("inf")
        flag = 0
        pos = 0
        for data in arr:
            if data==0:
                continue
            else:
                if data<0:
                    flag+=1
                    maxi = max(maxi,data)
                
                else:
                    pos = 1
                result*=data
        
        if result<0 and pos:
            return result//maxi
        return result
    
obj = Solution()

arr = [6, -3, -10, 0, 2]
n = len(arr)

print(obj.maxProduct(arr,n))