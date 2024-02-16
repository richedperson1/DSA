"""
! URL : https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""
from binary_tree import *
class Solution:
    def maxPathSum(self, root) -> int:

        self.result = -float("inf")
        self.sum = 0
        def dfs(root):
            if not root:
                return -100000
            if not(root.left and root.right):
                return root.val

            left = dfs(root.left)
            right = dfs(root.right)
            current_path = left+right+root.val
            self.result = max(self.result, current_path)
            return max(left+root.val,right+root.val)


        dfs(root)
        return root.val if self.result==float("inf") else self.result
    
null = -1
arr =[-10,9,20,null,null,15,7,8,9,null,null,9,null,18]+[-1]*5
root = createTree().createTreeUsingList(arr)
    
obj = Solution()
print(obj.maxPathSum(root))