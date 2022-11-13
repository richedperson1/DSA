arr = list(map(int, "0 2 1 2 0".split()))
n = len(arr)
zero = 0
two = n-1


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


def sorting_0s_1s_2s(arr):

    ind = 0
    zero = 0
    two = len(arr)-1
    while ind <= two:
        if arr[ind] == 0:
            swap(arr, ind, zero)
            zero += 1
            ind += 1
        elif arr[ind] == 2:
            swap(arr, ind, two)
            ind += 1
            two -= 1
        else:
            ind += 1

    return arr


sorting_0s_1s_2s(arr)
print(arr)
