# from optparse  check_choice


arr = []

n = len(arr)


def check_str(arr, i):
    if i <= 0:
        return True
    if i >= 1:
        # print(i)
        if arr[i] < arr[i-1]:
            return False

        return check_str(arr, i-1)
    # else:
    #     return True


print("Method 1 ")
# check_str(arr, n-1)
if check_str(arr, n-1):
    print("Array is sorted\n")
else:
    print("Array is Un-sorted\n")


def check_sort(arr):
    if len(arr) <= 1:
        return True

    elif arr[0] > arr[1]:
        return False

    return check_sort(arr[1:])


print("Method 2 ")
if check_sort(arr):
    print("Array is sorted")
else:
    print("Array is Un-sorted")


"""
checking sorting of array using pointer i
"""

brr = [1, -2]


def check_sort(arr, i):
    l = len(arr)
    if i == l-1 or i == l:
        return True
    elif arr[i] > arr[i+1]:
        return False

    return check_sort(arr, i+1)


print("Is array is sorted : ", check_sort(brr, 0))
