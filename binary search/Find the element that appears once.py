#User function Template for python3
class Solution:
    def search(self, n, arr):
        # your code here
        
        if n==0:
            return
        elif n==1:
            return arr[0]
        low = 0
        
        high = n
        
        ans = 0
        while low<high:
            mid = (low+high)//2
            
            if mid&1==1:
                if mid-1>-1 and  arr[mid-1]==arr[mid]:
                    low = mid+1
                else:
                    ans = arr[mid]
                    high = mid
            else:
                if mid+1<n and arr[mid+1]==arr[mid]:
                    low = mid+1
                else:
                    ans = arr[mid]
                    high = mid
        return ans

arr = [2,2,5,5,20,20,30]
n = len(arr)

obj = Solution()
print(obj.search(n,arr))