# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        def child_location(root):
            if not root:
                return False
            
            if root.val==x:
                return root
            
            first = child_location(root.left)
            if first:
                return first
            return child_location(root.right)
        
        def child_count(root):
            if not root:
                return 0
            
            return child_count(root.left)+child_count(root.right)+1
        node = child_location(root)
        left = child_count(node.left)
        right = child_count(node.right)
        remain = n-left-right-1

        return remain>left+right+1 or left>remain+right+1 or right>remain+left+1


        