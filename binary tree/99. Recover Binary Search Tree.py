from binary_tree import *

# The class `Solution` contains a method `recoverTree` that modifies a binary search tree in-place to
# recover it from being incorrectly swapped.

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
    def recoverTree2(self, root) -> None:
        start,prev,last = None,None,None
        def dfs(root):
            nonlocal start,last,prev
            if not root:
                return
            dfs(root.left)
            if prev and prev.val>root.val:
                if not start:
                    start = prev
                last = root
            prev = root
            dfs(root.right)
        
        dfs(root)
        if start and last:
            start.val,last.val = last.val,start.val
            
null = -1
arr = [5,3,10,6,null,2,11]
tree = createTree().createTreeUsingList(arr)
obj = Solution().recoverTree2(tree)
root.print_tree(tree)
            
# root.print_tree(obj)