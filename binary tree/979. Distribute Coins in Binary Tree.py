"""
!  URL : https://leetcode.com/problems/distribute-coins-in-binary-tree/
"""

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.step_need = 0

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right= dfs(root.right)
            self.step_need += abs(left)+abs(right)
            return left+right+root.val-1
        
        dfs(root)
        return self.step_need