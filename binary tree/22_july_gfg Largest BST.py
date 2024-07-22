from binary_tree import *
class Solution:
    def largestBst(self, root):
        # Your code here
        self.maxi = 1
        def dfs(root):
            if not root:
                return 0
                
            if root.left ==None and root.right==None:
                return 1
                
            left = dfs(root.left)
            right= dfs(root.right)
            
            
            if left and right:
                if root.data>root.left.data and root.data<root.right.data:
                    self.maxi = max(self.maxi,left+right+1)
                    return left+right+1
                
                return 1
            
            elif left :
                if root.left.data<root.data:
                    local = 1+left
                    self.maxi = max(self.maxi,local)
                    return local
                return 1
            elif right :
                if root.right.data>root.data:
                    local = 1+right
                    self.maxi = max(self.maxi,local)
                    return local
                return 1
            return left+right
        dfs(root)
        return self.maxi
    
    
arr = [10,5,15,13]
arr.extend([-1]*5)
treeNode = createTree().createTreeUsingList(arr)
print(Solution().largestBst(treeNode))
# root.print_tree(treeNode)