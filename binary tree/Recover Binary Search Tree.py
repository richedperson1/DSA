from binary_tree import *
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """ 
        ans = []
        def inorder(root):
            if not root:
                
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        
        inorder(root)
        print(ans)
        ans = sorted(ans)
        print(ans)
        
        self.ind = 0
        def inorder_tree(root):
            if not root:
                return
        
            inorder_tree(root.left)
            local = ans[self.ind]
            root.data = local
            self.ind+=1
            inorder_tree(root.right)
            
        inorder_tree(root)
        root.print_tree(root)
        return root
    
null = -1
arr = [1,3,null,null,2]
tree = createTree().createTreeUsingList(arr)
obj = Solution().recoverTree(tree)
            
# root.print_tree(obj)