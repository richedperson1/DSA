s = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def subarraySum(arr,  s):
    if s == 0:
        if 0 in arr:
            l = arr.index(0)
            return [l, l]
        else:
            return -1

    n = len(arr)
    i = 0
    j = 0
    total = 0
    while j < n:

        if arr[j] > s:
            total = 0
            j += 1
            i = j
            continue
        if arr[j]+total == s:
            return [i+1, j+1]

        while i < j and total+arr[j] > s:
            total -= arr[i]
            i += 1
        if arr[j]+total == s:
            return [i+1, j+1]
        total += arr[j]
        j += 1

    if total == s:
        return [i+1, j+1]
    else:
        return -1


print(subarraySum(arr, s))
