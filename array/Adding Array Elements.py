from heapq import heapify, heappop, heappush


def minOperations(arr, n, k):
    arr = sorted(arr)
    total = arr[0]
    if total >= k:
        return 0
    total += arr[1]
    if total >= k:
        return 1
    operation = 1

    for i in range(2, n):
        total += arr[i]
        operation += 1
        if total >= k:
            return operation
    # code here
    return -1


def minoperation_2(arr, n, k):
    if n == 1:
        return 0
    arr = sorted(arr, reverse=True)
    if arr[-1] >= k:
        return 0
    operation = 0
    while len(arr) > 1:
        first = arr.pop()
        second = arr.pop()
        arr.append(first+second)
        operation += 1
        if arr[-1] >= k:
            return operation
        arr = sorted(arr)
    if arr[-1] < k:
        return -1
    return operation

# class Solution:


def minOperations(arr, n, k):
    heapify(arr)
    count = 0
    for i in range(len(arr)):
        if arr[0] >= k:
            break

        res = heappop(arr) + heappop(arr)
        heappush(arr, res)
        print(arr)
        count += 1
    return count


n, k = 9, 7
arr = list(map(int, "7 3 7 1 8 10 1 5 6".split()))
# print(sorted(arr))
print(minoperation_2(arr, n, k))
