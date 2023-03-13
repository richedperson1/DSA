"""
URL : https://leetcode.com/problems/symmetric-tree/
"""
from collections import deque

"""
Recursive approach
Time complexity : O(n)
Space complexity : O(h)
"""


def isSymmetric(self, root) -> bool:

    def dfs(left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (left.val == right.val) and (dfs(left.left, right.right)
                                            and dfs(left.right, right.left))

    return dfs(root.left, root.right)


"""

Recursive approach
Time complexity : O(n)
Space complexity : O(h)

"""


def nonRecursive(root):
    if not root:
        return root

    queue = deque([root.left, root.right])

    while queue:
        left_node = queue.popleft()
        right_node = queue.popleft()

        if not(left_node) and not(right_node):
            return True
        if not(left_node) or not(right_node):
            return False

        if left_node.val != right_node.val:
            return False

        queue.append(left_node.left)
        queue.append(right_node.right)
        queue.append(left_node.right)
        queue.append(right_node.left)

    return True
