class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        i, j = 1, 0
        
        platform_needed = 1
        max_platforms = 1
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platform_needed += 1
                max_platforms = max(max_platforms, platform_needed)
                i += 1
            else:
                platform_needed -= 1
                j += 1
        return max_platforms
    
arr = [900, 1135, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000]


solve = Solution()
print(solve.minimumPlatform(arr, dep))  # Output: 3