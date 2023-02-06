"""
URL : https://leetcode.com/problems/shuffle-the-array/description/
"""

nums = [2, 5, 1, 3, 4, 7]
n = 3

"""
Brute force approach 

Time complexity : O(n)
Space complexity : O(n)

"""


def shuffle(nums: list[int], n: int) -> list[int]:
    final = []
    for ind in range(n):
        final.append(nums[ind])
        final.append(nums[ind+n])

    return final


"""
Optimize approach 

Time complexity : O(n)
Space complexity : O(1)

"""


def shuffleArr(arr: list[int], n: int) -> list[int]:
    for i in range(n):
        arr[i] = arr[i] << 10
        arr[i] = arr[i] ^ arr[i+n]

    actual = n*2 - 1
    for ind in range(n-1, -1, -1):
        first = arr[ind] & 1023
        arr[actual] = first
        actual -= 1
        second = arr[ind] >> 10
        arr[actual] = second
        actual -= 1

    return arr


shuffleArr(nums, n)
print(nums)
