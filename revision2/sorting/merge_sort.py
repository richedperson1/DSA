arr = [5, 4, 3, 1, 0, 8]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    high = len(arr)
    low = 0
    mid = (low+high)//2

    left = arr[low:mid]
    right = arr[mid:high]

    merge_sort(left)
    merge_sort(right)

    i = 0
    j = 0
    k = 0
    if len(arr) > 1:
        while i < len(left) and j < len(right) and k < len(arr):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            elif right[j] < left[i]:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


brr = arr.copy()
print(sorted(brr))
print(merge_sort(arr))


a = 2*2
