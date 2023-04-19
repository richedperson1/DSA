"""
URL : https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""

from binary_tree import *


def longZigZap(root):
    if not root:
        return 0

    def helper(root, prev, total):
        if not root:
            return total
        ans = 0
        if prev != -1:
            if prev == "l":
                l1 = helper(root.right, "r", total+1)
                l2 = helper(root.left, "l", 0)
                return max(l1, l2)

            else:
                l1 = helper(root.left, "l", total+1)
                l3 = helper(root.right, "r", 0)
                return max(l1, l3)
        else:
            l1 = helper(root.left, "l", 0)
            l2 = helper(root.right, "r", 0)
            return max(l1, l2)

    return helper(root, -1, 0)


ListNode = [1, -1, 1, 1, 1, -1, -1, 1,
            1, -1, 1, -1, -1, -1, 1, -1, 1]


headNode = createTree().createTreeUsingList(ListNode)


print(longZigZap(headNode))
