"""
from GFG Pratice set problem
 
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.

"""

# Naive Approach
# arr = [2, 1, 3, 1, 6, 0]
# arr = [2, 1, 4, 3, 5]


def check_invetion(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                total += 1

    return total


"""
Time complexity : O(n.log(n))
Space complexity : O(n)
"""

def checkInvetion(arr):

    totalAns = 0

    def inversionCount(arr):
        nonlocal totalAns
        if len(arr)<=1:
            return totalAns

        size = len(arr)

        left  = arr[:size//2]
        right = arr[size//2:]
        inversionCount(left)
        inversionCount(right)

        numI = len(left)
        numJ = len(right)
        numK = len(arr)
        i ,j,k = 0,0,0
        
        while i<numI and j<numJ:
            if left[i]>right[j]:
                totalAns+=(numI-i)
            a = 0
            if left[i]>right[j]:
                arr[k] = right[j]
                j+=1
            else:
                arr[k] = left[i]
                i+=1
            k+=1
        
        while i<numI:
            arr[k] = left[i]
            i+=1
            k+=1

        while j<numJ:
            arr[k] = right[j]
            j+=1
            k+=1

        return totalAns
    return  inversionCount(arr)    
   

arr = [1,8,3,2,1]
print(check_invetion(arr))
print(checkInvetion(arr))
