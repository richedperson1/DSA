from binary_tree import *
class Solution:
    def merge(self, root1, root2):
        # code here
        
        def inorder(root,first):
            if not root:
                return None
            
            inorder(root.left,first)
            first.append(root.data)
            inorder(root.right,first)
        
        first = []
        second = []
        inorder(root1,first)
        inorder(root2,second)
        
        final = []
        
        f = 0
        s = 0
        sizef = len(first)
        sizes = len(second)
        while f<sizef and s < sizes:
            if first[f]>=second[s]:
                final.append(second[s])
                s+=1
            
            else:
                final.append(first[f])
                f+=1
                
        while f<sizef:
            final.append(first[f])
            f+=1
        
        while s<sizes:
            final.append(second[s])
            s+=1
        return final
    

treeStr1 = "2 1 3 N N N 7 6 9 10 N 56 89 10 N N N 10 15 12"
treeStr2 = "5 3 6 2 4 N 5 N 6 4"

treeNode1 = createTree().createTreeUsingStrGFG(treeStr1)
treeNode2 = createTree().createTreeUsingStrGFG(treeStr2)

root.print_tree(treeNode1)
print("==================================")
root.print_tree(treeNode2)

