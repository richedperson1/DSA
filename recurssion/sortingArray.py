arr = [2, 4, 55, 10, 3, 6]


def sorting(arr, i):
    if i >= len(arr):
        return arr

    mini = i

    for j in range(i, len(arr)):
        if arr[j] < arr[mini]:
            mini = j

    arr[i], arr[mini] = arr[mini], arr[i]

    return sorting(arr, i+1)


print(sorting(arr, 0))

# check is array sorted ?

arr = [2, 3, 4, 15, 6]


def checkSorting(arr):
    if len(arr) <= 1:
        return True

    return arr[0] < arr[1] and checkSorting(arr[1:])


print(checkSorting(arr))
