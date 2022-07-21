def peakElement(arr, n):
    high = len(arr)-1
    low = 0
    if high == 0:
        return 0

    while low < high:
        mid = (low+high)//2

        if (mid > 0 and mid < high) and arr[mid-1] < arr[mid] > arr[mid+1]:
            return 1

        elif arr[mid] < arr[mid+1]:
            low = mid+1
        else:
            high = mid-1

    return low


arr = [1, 2, 3]
print(peakElement(arr, 3))
