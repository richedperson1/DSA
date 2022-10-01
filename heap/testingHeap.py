def swapIndex(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


def delte(arr, index):
    if index > len(arr):
        return arr

    leftInd = 2*index
    rgtInd = 2*index+1
    if rgtInd < len(arr)-1 and arr[index] < arr[rgtInd]:
        arr = swapIndex(arr, index, rgtInd)
        arr = delte(arr, rgtInd)

    elif leftInd < len(arr)-1 and arr[index] < arr[leftInd]:
        arr = swapIndex(arr, index, leftInd)
        arr = delte(arr, leftInd)
    return arr


arr = [0, 96, 55, 72, 50, 52, 53, 60]
arr[1] = arr[-1]
arr.pop()
print(delte(arr, 1))
