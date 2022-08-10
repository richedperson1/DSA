"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1

"""


class Solution:
    def nextGreaterElement(self, arr: int) -> int:
        arr = list(str(arr))
        flag = False
        i = len(arr)-1
        while i > 0 and arr[i] <= arr[i-1]:
            i -= 1
        if i <= 0:
            return -1

        j = i
        while j+1 < len(arr) and arr[j+1] > arr[i-1]:
            j += 1

        arr[j], arr[i-1] = arr[i-1], arr[j]
        arr[i:] = arr[i:][::-1]

        result = int("".join(arr))
        return result if result < (1 << 31) else -1


# for
num = 11

obj = Solution().nextGreaterElement(num)
print(obj)
