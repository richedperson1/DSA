"""
URL : https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
"""

from binary_tree import *

"""
The function `longZigZap` recursively calculates the length of the longest zigzag path in a binary
tree.

:param root: The `root` parameter in the `longZigZap` function is the root node of a binary tree.
The function `longZigZap` is trying to find the length of the longest zigzag path in the binary tree
:return: The function `longZigZap` is returning the result of calling the helper function with the
root node of a tree, an initial previous direction of -1, and a total count of 0. The helper
function recursively traverses the tree in a zigzag pattern and calculates the maximum length of the
zigzag path. The final result of the helper function is returned by the `longZ
"""

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


def longZipZag2(root):
    ans = 0
    def dfs(root):
        nonlocal ans
        if not root:
            return -1,-1
        
        left  = longZipZag2(root.left)[1]+1
        right = longZipZag2(root.right)[0]+1
        ans   = max(left,right,ans)
        return left,right

ListNode = [1, -1, 1, 1, 1, -1, -1, 1,
            1, -1, 1, -1, -1, -1, 1, -1, 1]


headNode = createTree().createTreeUsingList(ListNode)


print(longZigZap(headNode))
