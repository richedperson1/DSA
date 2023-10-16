"""
! URL : https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
"""
from queue import PriorityQueue

def smallestRange(arr):
    pq = PriorityQueue()
    maxi = -float('inf')
    result = [float("inf"),-float("inf")]
    for ind,data in enumerate(arr):
        local = (data[0],ind,0)
        pq.put(local)
        maxi = max(data[0],maxi)
    
    while pq.empty()!=True:
        pqData = pq.get()
        data,numInd,colInd = pqData
        if result[0]-result[1]> maxi-data:
            result[0] = maxi
            result[1] = data
            
        if colInd+1>=len(arr[numInd]):
            break
        
        newData = arr[numInd][colInd+1]
        pq.put((newData ,numInd,colInd+1))


        maxi = max(maxi,newData)
    print(result)

arr = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
smallestRange(arr)

    
    