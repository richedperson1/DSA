from binary_tree import root as TreeNode,createTree,root
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.ans = ""
        def dfs(root):
            if not root:
                self.ans+="#N"
                return 
            
            self.ans+= f"#{root.val}"
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans if len(self.ans)<=1 else self.ans[1:]
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        inorder = data.split("#")
        self.size = len(inorder)
        self.ind  = 0
        def dfs():
            if self.ind>=len(inorder) or inorder[self.ind]=="N":
                self.ind+=1
                return 
            
            root = TreeNode(data = inorder[self.ind])
            self.ind+=1
            root.left = dfs()
            root.right = dfs()
            return root
        final  = dfs()
        print(final)
        return final
    

null = -1
arr = [1,2,3,null,null,4,5]
arr = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
arr.extend([-1]*10)
arr = [1,2,3,null,null,4,5]
treeObj = createTree().createTreeUsingList(arr)
root.print_tree(treeObj)

obj = Codec()

result = obj.serialize(treeObj)
print(result)
root.print_tree(obj.deserialize(result))
