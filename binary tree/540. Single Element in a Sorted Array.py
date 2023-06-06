"""
URL : https://leetcode.com/problems/single-element-in-a-sorted-array/
"""


"""
Time complexity : O(n)
Space complexity : O(n)
"""


arr = [0,1,1,3,3,4,4,8,8]
ans = 0

def outPutBrute(arr):
    dist = {}

    for num in arr:
        dist[num] = dist.get(num,0)+1
    
    for key,val in dist.items():
        if val==1:
            return key
        

"""
Time complexity : O(n)
Space complexity : O(1)
"""

def outputOptimal(arr):

    if len(arr)<=1:
        return arr[0]

    ind = 0
    size = len(arr)
    while ind<size:
        if ind+1<size and arr[ind]!=arr[ind+1]:
            return arr[ind]

        ind+=2
    return arr[-1]

"""
Time complexity : O(log(n))
Space complexity : O(1)
"""


def outputOptimize(arr):
    if len(arr)<=1:
        return arr[0]
    
    low,high = 0,len(arr)-1

    while low<high:
        mid = (low+high)//2

        if mid&1:
            mid-=1
        
        if arr[mid]==arr[mid+1]:
            low = mid+2
        else:
            high = mid

    return arr[low]

    


def checking(output,ans):
    assert output==ans
    return "sucess"

output = outPutBrute(arr)
output = outputOptimize(arr)

print(checking(output,ans))
print(output)