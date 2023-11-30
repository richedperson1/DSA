class Solution:
    def findMin(self, arr: list[int]) -> int:
        if len(arr)<=1 or arr[0]<arr[-1]:
            return arr[0]
        if len(arr)==2:
            return min(arr)
        size = len(arr)
        low,high=0,size-1
        ans = float("inf")
        while low<=high:
            mid = (low+high)//2
            ans = min(ans,arr[mid])
            if mid+1<size and arr[mid-1]>arr[mid]<arr[mid+1]:
                return arr[mid]

            elif arr[mid]>=arr[0]:
                low = mid+1
            else:
                high = mid-1

        return ans if ans<float("inf") else -1

            
            
arr = [5,1,2,3,4]
obj = Solution()
print(obj.findMin(arr))