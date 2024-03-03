from binary_tree import *

class Solution:
    def deleteNode(self, root, key: int):
        def dfs(root,key,parent = None):
            if not root:
                return root

            if root.val>key:
                root.left = dfs(root.left,key,root)
            elif root.val<key:
                root.right = dfs(root.right,key,root)
            else:
                
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
 
                curr = root.right
                prev = None
                while curr.left:
                    prev = curr
                    curr = curr.left
                

                tempL = root.left
                tempR = root.right
                # root.val = curr.val
                if prev==None:
                    root.right = curr.right
                    tempR = root.right
                else:
                    prev.left = curr.right
                
                if parent and parent.left==root:
                    parent.left = curr
                    curr.left = tempL
                    curr.right = tempR

                if parent and parent.right==root:
                    parent.right = curr
                    curr.left = tempL
                    curr.right = tempR
                root = curr
            return root

        return dfs(root,key)
    

null = -1
arr = [15,7 ,25,3,10,null,null,null,null,8,12,null,9]

obj = Solution()
tree = createTree().createTreeUsingList(arr)
root.print_tree(obj.deleteNode(tree,7))