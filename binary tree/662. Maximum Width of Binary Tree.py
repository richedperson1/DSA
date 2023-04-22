"""
URL : https://leetcode.com/problems/maximum-width-of-binary-tree/
"""


from binary_tree import *


def maxWidth(root):
    def dfs(root, prev):
        if not root:
            return 0

        left = dfs(root.left, prev)
        right = dfs(root.right, prev)

        if prev == "l":
            if left < right:
                return right

            return left+1

        else:
            if right < left:
                return left
            return right+1

    leftCall = dfs(root.left, "l")
    rightCall = dfs(root.right, "r")
    print(leftCall, rightCall)
    return rightCall+leftCall


# rootList = [1, 3, 2, 5, 3, -1, 9]
# rootList = [1, 3, 2, 5, -1, -1, 9, 6, -1, 7]
# nodeTree = createTree().createTreeUsingList(rootList)
# print(maxWidth(nodeTree))


a = 5
b = a
c = 5
d = "5"
f = f"{d}"

g = f"{a}"
e = f"{a}"


# print("d : ", id(d))
# print("f : ", id(f))
print("e : ", id(e))
print("g : ", id(g))
