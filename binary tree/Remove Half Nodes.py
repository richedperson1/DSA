from binary_tree import *
class Solution:
    def RemoveHalfNodes(self, node):
        #code here
        
        def dfs(root):
            if not root:
                return 
            
            if not root.left and not root.right:
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            
            if root.left and root.right:
                root.left = left
                root.right = right
                return root
            else:
                return left or right
        return dfs(node)
    

arr = list(map(int,"5 7 8 2".split()))
arr.extend([-1]*5)
treeNode = createTree().createTreeUsingList(arr)

obj = Solution()

new_Tree = obj.RemoveHalfNodes(treeNode)

root.print_tree(new_Tree)