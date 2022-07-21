import sys
import copy

arr = [2, 1, 3, 4, 5, 6, 7, 8]


def reverse(arr, i, j):
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
        reverse(arr, i+1, j-1)

    return arr


print(reverse(arr, 0, len(arr)-1))  # In this we give array by referance only
print(arr)

# ------------------------------------------------------------------------------------------------ #
array = [2, 1, 3, 4, 5, 6, 7, 8]
arr = copy.copy(array)


def reverse_copy(arr, i, j):
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]
        reverse(arr, i+1, j-1)

    return arr


print(reverse_copy(array, 0, len(array)-1))

# ------------------------------------------------------------------------------------------------ #
# Reverse array by using single pointer
print("="*50)
array = [2, 1, 3, 4, 5, 6, 7, 8]
arr = copy.copy(array)


def reverse_copy_using_1_var(arr, i):
    if i < len(arr)-1-i:
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
        reverse_copy_using_1_var(arr, i+1)
    return arr


print(reverse_copy_using_1_var(array, 0))
print(arr)
print("="*50)
print("The referance count of array is : ", sys.getrefcount('a'))


# ---------------------------------------------------------------- #


string = "mam"


def check_palimdrom(string, i, j, flag):
    if i < j:
        flag = string[i] == string[j]
        check_palimdrom(string, i+1, j-1, flag)
        if flag == False:
            return flag
    return flag


print(check_palimdrom(string, 0, len(string)-1, False))
