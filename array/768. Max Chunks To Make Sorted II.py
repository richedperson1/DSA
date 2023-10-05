
"""
! URL : https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
"""
def maxChunksToSorted( arr: list[int]) :
    size = len(arr)
    mini = [float('inf')]*(size+1)
    
    maxi = [0]*size
    localMax = 0
    localMin = float('inf')
    for ind in range(size):
        localMax= max(localMax,arr[ind])
        maxi[ind] = localMax

        localMin = min(arr[-(ind+1)],localMin)

        mini[-(ind+2)] = localMin

    count = 0
    for ind in range(size):
        maxiInd = maxi[ind]
        miniInd = mini[ind+1]
        if maxiInd<=miniInd:
            count+=1

    return count
            




arr = [2,3,4,1,2,6]
arr = [0,2,3,81,9]
print(maxChunksToSorted(arr))




print()