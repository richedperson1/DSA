"""
Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

"""
arr = [1, 7, 7, 7]
k = 7

n = len(arr)


def check_index(arr, k):
    if len(arr) == 0:
        return -1

    elif arr[-1] == k:
        return 0

    arr.pop()
    small = check_index(arr, k)
    if small == -1:
        return -1
    else:
        # small += 1
        # small = n-small
        return n-small


def check_index_b(arr, i, k):
    if i < 0:
        return -1
    if arr[i] == k:
        return i

    return check_index_b(arr, i-1, k)


print(check_index_b(arr, len(arr)-1, k))
print(check_index(arr,  k))
