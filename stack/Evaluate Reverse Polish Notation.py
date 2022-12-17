"""
URL : https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

tokens = ["2"]

stack = []

operator = ["+", "-", "*", "/"]

for data in tokens:
    if data in operator:
        first = int(stack.pop())
        second = int(stack.pop())
        index = operator.index(data)
        if index == 0:
            result = second+first
        elif index == 1:
            result = second-first
        elif index == 2:
            result = second*first
        else:
            result = second/first
        stack.append(result)
    else:
        stack.append(data)

print(stack[0])
