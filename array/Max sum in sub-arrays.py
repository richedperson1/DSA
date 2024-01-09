class Solution:
    def pairWithMaxSum(self, arr, N):
        
        first,second = -float("inf"),-float("inf")
        
        for data in arr:
            if first<data:
                second = first
                first = data
            elif second<data and first>data:
                second = data
                
        return first+second
        
        
    
    
obj = Solution()

arr = [1,2,3,4,5,6]
n = len(arr)
print(obj.pairWithMaxSum(arr,n))