def middleNum(arr1,arr2,midNum) :
    ind1=ind2 = 0
    sizeA,sizeB = len(arr1),len(arr2)
    middle = 0
    while ind1 < sizeA and ind2 < sizeB:
        if arr1[ind1]>arr2[ind2]:
            middle+=1
            if middle==midNum:
                return  arr2[ind2]
            ind2+=1
        else:
            middle+=1
            if middle==midNum:
                return arr1[ind1] 
            ind1+=1
    
    while ind1< sizeA :
        middle+=1
        if middle==midNum:
            return arr1[ind1]
        ind1+=1

    while  ind2 < sizeB :
        ind2+=1
        middle+=1
        if middle==midNum:
            return arr2[ind2]
            

def findMedianSortedArrays( nums1: list[int], nums2: list[int]) :
    
    sizeA = len(nums1)
    sizeB = len(nums2)

    total = sizeA + sizeB

    if total&1==0:
        mid1 = total//2
        mid2 = (total//2) +1
        firstOut = middleNum(nums1,nums2,mid1)
        secondOut = middleNum(nums1,nums2,mid2)
                    
        return(firstOut+secondOut)/2
    else:
        return middleNum(nums1,nums2,total//2+1)



arr = [1,2]
brr = [7,8]

print(findMedianSortedArrays(arr,brr))