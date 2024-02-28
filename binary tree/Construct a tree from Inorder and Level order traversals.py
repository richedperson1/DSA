from binary_tree import *

    
    
def solve(lev,i):
    rooting=None
    if i<len(lev):
        rooting=root(lev[i])
        rooting.left=solve(lev,2*i+1)
        rooting.right=solve(lev,2*i+2)
    return rooting  
        

            

def buildTree(level, ino):
    return solve(level,0)


inorder = [4, 8, 10, 12, 14, 20, 22]
level   = [20, 8, 22, 4, 12, 10, 14]

inorder = [8,7,20,18,22]
level   = [20,8,22,7,18]

root.print_tree(buildTree(level,inorder))