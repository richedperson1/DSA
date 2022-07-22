s = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# method 1


def naive_solution(arr, s):
    n = len(arr)
    for i in range(n):
        local1 = arr[i]
        for j in range(i+1, n):
            local1 += arr[j]
            if local1 == s:
                return [i+1, j+1]
            elif local1 > s:
                break
    return [-1]

# method 2


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


s = 18
arr = [1, 2, 3, 7, 5]
print(naive_solution(arr, s))
print(subarraySum(arr, s))
