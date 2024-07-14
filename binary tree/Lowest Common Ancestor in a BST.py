#Function to find the lowest common ancestor in a BST. 
from binary_tree import *
def LCA(root, n1, n2):
    #code here.
    lst = [0]
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right= dfs(root.right)
        if left+right==3:
            lst[0] = root
            return 0
            
        elif (left==1 or right==1) and root.data==n2:
            lst[0] = root
            return 0
            
        elif (left==2 or right==2) and root.data==n1:
            lst[0] = root
            return 0
            
        elif root.data==n1:
            return 1
        
        elif root.data==n2:
            return 2
        
        else:
            return left+right
    
    final = dfs(root)
    
    return lst[0] 
arr = list(map(int,"15 5 20 2 13 17 25 1 3 8 14".split()))
treeNode = createTree().createTreeUsingList(arr)

# root.print_tree(treeNode)


print(LCA(treeNode,8,17))