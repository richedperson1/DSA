def threeSum( nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    n = len(nums)
    for ind in range(1,n):
        if ind==0:
            continue
        small,large = ind-1,n-1
        sumi = nums[ind]+nums[small]+nums[large]
        while small < ind < large:
            if sumi>0:
                large-=1
            elif sumi<0:
                small+=1
            else:
                ans.append([nums[small],nums[ind],nums[large]])

                while small>=0 and nums[small]==nums[small-1]:
                    small+=1
                
                while large >ind and nums[large]==nums[large-1]:
                    large-=1

                small+=1
                large-=1

    return ans


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))