arr = [2, 1, 3, 5,  7]
brr = [2, 1, 3, 5, 9]


def joining_array(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = right[j]
            j += 1
            k += 1
        else:
            arr[k] = left[i]
            i += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def divide_1(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    right = arr[mid:]
    left = arr[0:mid]
    divide_1(right)
    divide_1(left)
    joining_array(left, right, arr)


def divide_2(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    right = arr[mid:]
    left = arr[0:mid]
    divide_2(right)
    divide_2(left)
    # concer(left, right, arr)
    l = 0
    r = 0
    i = 0
    while l < len(left) and r < len(right):
        if left[l] >= right[r]:
            arr[i] = right[r]
            i += 1
            r += 1
        else:
            arr[i] = left[l]
            i += 1
            l += 1
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        arr[i] = right[r]
        i += 1
        r += 1
    return arr


divide_1(arr)
divide_2(brr)
print(arr)
print(brr)
