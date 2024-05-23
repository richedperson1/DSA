class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        size = len(nums)
        def dfs(ind,arr):
            if ind>= size:
                total = 0
                for data in arr:
                    total^=data
                
                return total

            picked = dfs(ind+1,arr+[nums[ind]])
            nonpicked = dfs(ind+1,arr)
            
            return picked+nonpicked
        
        return dfs(0,[])
    
    
brr = [1,2,3,4,5,6,7,8,9,10,11,12]
obj = Solution()

print(obj.subsetXORSum(brr))