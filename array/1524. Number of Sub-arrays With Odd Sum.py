

def subArrayWithOdd(ind, arr, prefix):
    n = len(arr)
    if ind >= n:
        if prefix & 1:
            return 1
        return 0

    first = subArrayWithOdd(ind+1, arr, prefix+arr[ind])
    second = subArrayWithOdd(ind+1, arr, prefix)
    return first+second


def subArrayWithOdd2(ind, arr):
    n = len(arr)
    if ind >= n:
        return 0

    first = subArrayWithOdd2(ind+1, arr)+arr[ind]
    second = subArrayWithOdd2(ind+1, arr)+0

    return first+second


arr = [1, 3, 5]
print(subArrayWithOdd(0, arr, 0))
