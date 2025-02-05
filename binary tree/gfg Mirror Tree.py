# The `Solution` class contains two methods, `mirror1` and `mirror2`, which are used to convert a
# binary tree into its mirror tree using depth-first search.

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror1(self, root):
        # Code here
        def dfs(root):
            if not root:
                return 
            root.left,root.right = root.right,root.left
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return root
    def mirror2(self, root):
        # Code here
        def dfs(root):
            if not root:
                return 
            
            # root.left,root.right = root.right,root.left
            left = dfs(root.left)
            right= dfs(root.right)
            
            root.right = left
            root.left = right
            return root
        return dfs(root)