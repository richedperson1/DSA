s = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# method 1


def naive_solution(arr, s):
    n = len(arr)
    for i in range(n):
        local1 = 0
        for j in range(i, n):
            local1 += arr[j]
            if local1 == s:
                return [i+1, j+1]
            if local1 > s:
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


def subarraySum_without_space(arr, k):
    n = len(arr)
    for i in range(n):
        local = 0
        for j in range(i, n):
            local += arr[j]
            if local == k:
                return [i+1, j+1]
    return -1, -1


def subarraySum_with_space(arr, k):
    sumi = 0
    dist = {0: 0}
    n = len(arr)
    for i in range(n):
        sumi += arr[i]
        diff = sumi-k
        if diff in dist:
            return dist[diff], i
        else:
            dist[sumi] = i+1

    return -1


def subArraySum_without_space(arr, s):
    begin = 0
    end = 0
    n = len(arr)
    curr_sum = arr[begin]

    while begin != n:

        if curr_sum == s:
            return begin + 1, end + 1

        elif curr_sum < s and end < n-1:
            end += 1
            curr_sum += arr[end]

        elif begin == end and end < n-1:
            end += 1
            curr_sum += arr[end]

        else:
            curr_sum -= arr[begin]
            begin += 1

    return [-1]


s = 13
arr = [2, 5, 8]
print(subArraySum_without_space(arr, s))
