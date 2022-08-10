arr = [3, 2, 3, 2]

k = len(arr)//3

"""
Space complexity O(1)
Time complexity O(n^2)
"""


def naive_method(arr):
    n = len(arr)
    for i in range(n):
        local = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                local += 1

        if local > k:
            return arr[i]

    else:
        return -1


"""
Space complexity O(n)
Time complexity O(n)
"""


def using_space(arr):
    k = len(arr)//3
    dist = {}
    ans = []
    for i in arr:
        if i in dist:
            dist[i] += 1
            if dist[i] > k:
                ans.append(i)
        else:
            dist[i] = 1
            if dist[i] > k:
                ans.append(i)
    return ans


"""
Space complexity O(1)
Time complexity O(n.log(n))

Note:
Only useful when order of array not matter's
"""


def using_time(arr):
    arr = sorted(arr)
    count = 1
    i = 1
    while i < len(arr):
        if arr[i] == arr[i-1]:
            count += 1
            if count > k:
                return arr[i]
        else:
            count = 1
        i += 1
    return -1


arr = [1, 2]
print(naive_method(arr))
print(using_space(arr))
print(using_time(arr))
