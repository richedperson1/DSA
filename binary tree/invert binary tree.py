"""
URL : https://leetcode.com/problems/invert-binary-tree/
"""
from collections import *


def invertTree(root):
    if not root:
        return

    temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.right)
    invertTree(root.left)
    return root


def invertTreeQ(root):
    if not root:
        return root

    queue = deque([root])
    temping = root
    while queue:
        temp = queue.popleft()
        temp.left, temp.right = temp.right, temp.left
        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)

    return temping
