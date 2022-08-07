arr = [46541, 654685, 418, 8, 4, 18, 48, 498,
       0, -5, 645, 64, 4, 51, 68, 481, 8, -48, 1, 5]


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def pivot_elements(arr, si, ei):
    count = 0
    i = si+1
    for i in range(si, ei+1):
        if arr[si] > arr[i]:
            count += 1

    arr[si+count], arr[si] = arr[si], arr[si+count]

    pivot = si+count
    # i = si

    while si <= ei:
        if arr[si] < arr[pivot]:
            si += 1
        elif arr[ei] >= arr[pivot]:
            ei -= 1
        else:
            swap(arr, si, ei)
            si += 1
            ei -= 1

    return pivot


def quick_sort(arr, s, e):
    if len(arr) <= 1:
        return arr
    if s >= e:
        return arr

    i = pivot_elements(arr, s, e)
    quick_sort(arr, s, i-1)
    quick_sort(arr, i+1, e)
    return arr


brr = sorted(arr)
print(quick_sort(arr, 0, len(arr)-1) == brr)
