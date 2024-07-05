from binary_tree import *

def verticalWidth(root):
    # code here
    maxi = set()
    def width(root,total):
        if not root:
            return abs(total)
            
        
        
        maxi.add(total)
        left = width(root.left,total-1)
        right = width(root.right,total+1)
        
        return maxi
    
    width(root,0)
    return maxi


arr = list(map(int,"1 2 3 4 5 6 7 -1 -1 -1 -1 -1 8 -1 9".split()))
treeNode = createTree().createTreeUsingList(arr)


print(verticalWidth(treeNode))