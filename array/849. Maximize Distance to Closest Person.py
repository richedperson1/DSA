"""
! URL : https://leetcode.com/problems/maximize-distance-to-closest-person/
"""

"""
Time complexity : O(n)
Space complexity : O(n)
"""
def maxDistToClosest( arr) -> int:
    size = len(arr)
    leftFilled = [ind for ind in range(size)]

    lastNum = -1
    for ind in reversed(range(size)):
        if arr[ind]==1:
            lastNum = ind
        leftFilled[ind] = lastNum

    
    left2right = -1

    maxi = 0
    ansInd = None
    for ind,data in enumerate(arr):
        if data==1:
            left2right = ind
            continue

        if left2right==-1 and leftFilled[ind]==-1:
            continue

        elif left2right==-1 and leftFilled[ind]!=-1:

            leftD = leftFilled[ind]-ind
            rightD = size

            if maxi<min(leftD,rightD):
                maxi = min(leftD,rightD)
                ansInd = ind
    
        elif leftFilled[ind]== -1 and left2right!=-1:

            if maxi< ind-left2right:
                maxi = ind-left2right
                ansInd = ind
        else:
            leftD = leftFilled[ind]-ind
            rightD= ind-left2right

            if maxi<min(leftD,rightD):
                maxi = min(leftD,rightD)
                ansInd = ind
    
    return maxi

"""
Time complexity : O(n)
Space complexity : O(1)
"""

def maxDistToClosestOptimize( seats: list[int]) -> int:
    result,prev = 0,-1
    size = len(seats)
    for ind in range(size):
        if seats[ind]:
            local = ind if prev== -1 else (ind-prev)//2
            result = max(result,local)
            prev = ind

    return max(result,size-prev-1)

"""
Test Case : 
[1,0,0,0,1,0,1]
[1,0,0,0]
[0,0,0,1,0,0,0]
[0,1,0,0,0,1]
[0,1]
[0,1,0,0,0,0,0,0]
[0,0,1]
[1,0,0,0,0,0,0]
[1,0,0,1]
"""

arr = [0,0,1]
print(maxDistToClosest(arr))