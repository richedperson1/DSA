arr = [1, 1, 1, 1]

n = len(arr)
k = 2


def naive_approach(arr, n):
    total = 0
    for i in range(n):
        sumi = arr[i]
        for j in range(i+1, n):
            if sumi+arr[j] == k:
                total += 1
    return total


def better_option(arr):
    """
    Time Complexity : O(n.log(n))
    Space Complexity
    """
    arr = sorted(arr)
    low = 0
    high = len(arr)-1
    total = 0
    while low < high:
        if (arr[low]+arr[high]) == k:
            total += 1
            low += 1
            high -= 1
        elif (arr[low]+arr[high]) > k:
            high -= 1
        else:
            low += 1
    return total


def optimize_option(arr, n):
    total = 0
    dist = {}
    for ind, data in enumerate(arr):
        want = k - data
        if want in dist:
            total += dist[want]
        if data in dist:
            dist[data] += 1
        else:
            dist[data] = 1
    return total


print(naive_approach(arr, n))
print(better_option(arr))
print(optimize_option(arr, n))
