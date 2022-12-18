"""
URL : https://leetcode.com/problems/daily-temperatures/description/
"""


"""
Time complexity : O(n)
space complexity : O(n)
"""


def dailyTemperatures(arr: list[int]) -> list[int]:
    num = len(arr)
    stack = []
    ans = []
    for ind in range(num-1, -1, -1):
        if len(stack) == 0:
            ans.append(0)
            stack.append(ind)

        while len(stack) > 0 and arr[stack[-1]] <= arr[ind]:
            stack.pop()

        if stack:
            local = stack[-1]-ind
            ans.append(local)
            stack.append(ind)
        else:
            ans.append(0)
            stack.append(ind)

    return ans[::-1][:-1]
