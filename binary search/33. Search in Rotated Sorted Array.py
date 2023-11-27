
class Solution:
    def search(self, arr: list[int], target: int) -> int:
        
        low,high = 0,len(arr)-1

        while low<=high:
            mid = (low+high)//2
            if arr[mid]==target:
                return mid

            else:
                if arr[0]<=arr[mid]:
                    
                    if arr[mid]>=target and arr[0]<=target:
                        high = mid-1
                    else:
                        low = mid+1
                else:
                    if arr[mid]<=target and arr[high]>=target:
                        low = mid+1
                    else:
                        high = mid -1

        return -1
    
    
obj = Solution()

arr = [7,1,3]
print(obj.search(arr,1))