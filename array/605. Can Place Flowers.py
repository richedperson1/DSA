"""
URL : https://leetcode.com/problems/can-place-flowers/
"""

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""
arr = [1, 0, 0, 0, 1]


def canPlaceFlowers(arr: list[int], n: int) -> bool:
    start = 0
    num = len(arr)

    for ind in range(start, num):
        if arr[max(ind-1, 0)] == 0 and arr[ind] == 0 and arr[min(ind+1, num-1)] == 0:
            arr[ind] = 1
            n -= 1

        if n <= 0:
            return True

    return n <= 0


print(canPlaceFlowers(arr, 1))
