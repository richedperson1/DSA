
arr = [12, 33, 4, 5, 6]


def printMin(arr, miniForNow=arr[0]):
    if len(arr) == 1:
        newMin = min(arr[0], miniForNow)
        print(newMin)
        return

    newMin = min(miniForNow, arr[0])

    printMin(arr[1:], newMin)


printMin(arr)
