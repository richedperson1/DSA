from binary_tree import *

def dfs(rooting,total):
    if not rooting:

        return False
    
    total-= rooting.data
    if total==0 and rooting.left==None and rooting.right==None:
        return True
    
    left = dfs(rooting.left,total+rooting.data)
    right= dfs(rooting.right,total+rooting.data)
    
    if left or right:
        return True
    
    return False
        
        

arr = list(map(int,"1 2 3 -1 -1 4 6 -1 5 -1 -1 7 -1".split()))

 
treeNode = createTree().createTreeUsingList(arr)

root.print_tree(treeNode)
target = 13
print(dfs(treeNode,target))
