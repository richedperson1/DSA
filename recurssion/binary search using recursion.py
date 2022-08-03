arr = [2, 3, 4, 5, 6, 8, 11, 25]
k = 60
n = len(arr)
low = 0


def binary_seach(arr, low, high, k):
    if low > high:
        return -1
    mid = (low+high)//2
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binary_seach(arr, low, mid-1, k)

    else:
        return binary_seach(arr, mid+1, high, k)


index = binary_seach(arr, low, n-1, k)
print("Number", k, f"present at {index} index")
print(index, "----------->", arr[index])
print("low value is ", low)
