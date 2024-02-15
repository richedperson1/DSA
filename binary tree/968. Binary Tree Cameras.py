from binary_tree import *
class Solution:
    def minCameraCover(self, root) -> int:
        if not root:
            return 0
        self.total = 0
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right= dfs(root.right)
            if left==1 or right==1:
                self.total+=1
                return 2
            elif left==2 or right==2:
                return 0
            else:
                return 1

        ans = self.total+1 if dfs(root)==1 else self.total
        return ans
    
    
null = -1
arr = [0,0,null,0,0]
tree = createTree().createTreeUsingList(arr)

root.print_tree(tree)