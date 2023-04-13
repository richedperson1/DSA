"""
URL : https://leetcode.com/problems/validate-stack-sequences/

"""

# Method 1

"""
Time complexity : O(n)
space complexity : O(n)

"""


def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:

    ans = []
    j = 0
    n = len(popped)
    for ind, data in enumerate(pushed):
        if pushed[ind] != popped[j]:
            ans.append(data)

        else:

            flag = False
            ans.append(data)
            while j < n and ans and ans[-1] == popped[j]:
                flag = True
                ans.pop()
                j += 1

            if flag == False:
                return False

    while j < n:
        if ans[-1] == popped[j]:
            ans.pop()
            j += 1
        else:
            return False
    return True


# Method 2
"""
Time complexity : O(n)
space complexity : O(1)

"""


def valid_stack(pushed, popped):
    i = 0
    j = 0

    for val in pushed:
        pushed[i] = val

        while i >= 0 and pushed[i] == popped[j]:
            i -= 1
            j += 1

        i += 1

    return not bool(i)
