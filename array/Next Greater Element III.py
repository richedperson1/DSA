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
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        flag = False
        for i in range(len(n)-1, 0, -1):
            if int(n[i]) > int(n[i-1]):
                flag = True
                n[i], n[i-1] = n[i-1], n[i]

        if flag == False:
            return -1

        ret = int(''.join(n))

        return ret if ret < 1 << 31 else -1

# for


obj = Solution().nextGreaterElement(21)
print(obj)
