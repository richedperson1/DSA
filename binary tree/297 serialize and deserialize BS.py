from binary_tree import *
class Codec:

    def serialize(self, root):
        ans = []
        def DFS(root):
            if not root:
                ans.append("N")
                return
            ans.append(str(root.val))
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return ",".join(ans)        

    def deserialize(self, data):
        value = data.split(",")
        self.index = 0
        def DFS():
            if value[self.index] == "N":
                self.index += 1
                return None
            root = TreeNode(int(value[self.index]))
            self.index += 1
            root.left = DFS()
            root.right = DFS()
            
            return root
        return DFS()                               

null = -1
    
arr = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]

arr.extend([-1]*10)
treeObj = createTree().createTreeUsingList(arr)
# root.print_tree(treeObj)

obj = Codec()

print(obj.serialize(treeObj))