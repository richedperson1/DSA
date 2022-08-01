arr = [1, 2, 3, 4, 5, 7]
k = 7

# Method 1
"""
In this methods extra space is require to store array
it will also modified array 
"""


def check_element(arr, k):
    l = len(arr)
    if l == 0:
        return -1

    elif arr[0] == k:
        return 0

    small_list = check_element(arr[1:], k)
    if small_list == -1:
        return -1
    else:
        return small_list+1


print(check_element(arr, k))

# Method 1


def check_element_better(arr, i, k):
    # l = len(arr)
    if i >= len(arr) or len(arr) == 0:
        return -1

    elif arr[i] == k:
        return i

    small_list = check_element_better(arr, i+1, k)
    return small_list


print(check_element_better(arr, 0, k))
