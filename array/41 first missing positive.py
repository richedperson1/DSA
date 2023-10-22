"""

! URL : https://leetcode.com/problems/first-missing-positive/description/

"""

def firstMissingPositive( nums:list[int]) -> int:
    nums.sort()
    size = len(nums)
    find = 1

    ind = 0 
    while ind<size:
        if nums[ind]<=0:
            ind+=1
            continue

        elif nums[ind]>find:
            return find

        else:
            while ind<size and find==nums[ind]:
                ind+=1
            find+=1
        
    return nums[-1]+1 if nums[-1]+1 >0 else 1

def firstMissingPositive2( nums:list[int]) -> int:
    flag = True
    for ind,data in enumerate(nums):
        if data<0:
            nums[ind] = 0
        else:
            flag = False

    if flag:
        return 1
    size = len(nums)
   
    for ind,data in enumerate(nums):
        if 1<= abs(data)<=size:
            value = abs(data)
            if nums[value-1]>0:
                nums[value-1]*=-1
            elif nums[value-1]==0:
                nums[value-1] = -1*(size+1)

    print(nums)
    for ind in range(1,size+1):
        if nums[ind-1]>=0:
            return ind
    
    return size+1 if flag else size

arr = [1,1,1,2,2,3,3,4,5,6,8]
arr = [-1,-2,-60,40,43]
arr = [3,4,-1,1]


print(firstMissingPositive2(arr))