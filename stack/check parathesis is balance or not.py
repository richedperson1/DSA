"""
URL : https://leetcode.com/problems/valid-parentheses/
"""


def ispar(x):
    # code here
    arr = [x[0]]
    x = x[1:]
    for ind, data in enumerate(x):

        if data == "[" or data == "(" or data == "{":
            arr.append(data)
        else:
            if data == "}" and len(arr) > 0 and arr[-1] == "{":
                arr.pop()

            elif data == ")" and len(arr) > 0 and arr[-1] == "(":
                arr.pop()

            elif data == "]" and len(arr) > 0 and arr[-1] == "[":
                arr.pop()
            else:
                return False

    if len(arr) == 0:
        return True

    return False


def checking_valid_bracket(s):

    dist = {")": "(", "}": "{", "]": "["}

    opening = "({["
    stack = []
    for br in s:
        if br in opening:
            stack.append(br)

        elif stack and stack[-1] == dist[stack[-1]]:
            stack.pop()
        else:
            return False

    return stack == []


chec = "({[]})"
print(ispar(chec))
