"""
URL : https://leetcode.com/problems/number-of-zero-filled-subarrays/
"""


# Method 1
"""
Time complexity : O(n)
Space complexity : O(1)
"""


def zeroFilledSubarray(nums: list[int]):
    final = 0
    rolling_zero = 0
    for ind, data in enumerate(nums):
        if data == 0:
            rolling_zero += 1
        else:
            ans = (rolling_zero*(rolling_zero+1))//2
            final += ans
            rolling_zero = 0

    if rolling_zero:
        ans = (rolling_zero*(rolling_zero+1))//2
        final += ans
    return final


# Method 2

"""
Time complexity : O(n)
Space complexity : O(1)
"""


def zeroFilledSubarray2(nums: list[int]):
    final = 0
    rolling_zero = 0
    for ind, data in enumerate(nums):
        if data == 0:
            rolling_zero += 1
        else:
            rolling_zero = 0

        final += rolling_zero


arr = [0, 0, 0, 2, 0, 0]
zeroFilledSubarray2(arr)
# print(zeroFilledSubarray(arr))
