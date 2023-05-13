"""
URL : https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
"""


arr1 = [1, 2,3]
arr2 = [4 ,5,14, 15]


num1 = len(arr1)
num2 = len(arr2)


def sortedArrayInplace(arr1,arr2):
    num1 = len(arr1)
    i1 = num1 - 1
    i2 = 0
    while arr1[i1]>arr2[i2]:
        arr2[i2],arr1[i1] = arr1[i1] ,arr2[i2]
        i1-=1
        i2+=1

    
    print(sorted(arr1),sorted(arr2))
    arr1.extend(arr2)
    print(sorted(arr1))
    

sortedArrayInplace(arr1,arr2)
