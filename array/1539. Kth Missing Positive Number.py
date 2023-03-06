"""
URL : https://leetcode.com/problems/kth-missing-positive-number/
"""


"""
Time complexity : O(n)
Space complexity : O(1)
"""


def findKthPositive(arr: list[int], k: int):
    total_k = 0
    ind = 0
    n = arr[-1]
    for i in range(1, n+1):
        if arr[ind] == i:
            ind += 1
        else:
            total_k += 1
            if total_k == k:
                return i

    require = k-total_k
    for i in range(n, n+require):
        total_k += 1
        if total_k == k:
            return i+1


"""
Time complexity : O(log(n))
Space complexity : O(1)
"""


def findKthPositiveOpt(arr, k):
    total = 0
    low, high = 0, len(arr)-1
    prev_low = 0
    while low <= high:
        mid = (low+high)//2
        require = arr[mid]-mid-1

        total = require
        if total < k:
            low = mid+1
        else:
            high = mid-1

    print(high)
    return high+k+1


arr = [2, 3, 4, 7, 11]
k = 5
print(findKthPositiveOpt(arr, k))
