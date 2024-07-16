
from typing import Optional,List
from binary_tree import *
class Solution:
    def getDirections(self, root: Optional, start: int, dest: int) -> str:

        
        def path_finder(root,val,path):
            if root.val==val:
                return True

            if root.left and path_finder(root.left,val,path):
                path+="L"
                return path
            
            if root.right and path_finder(root.right,val,path):
                path+="R"
                return path
            return False
        s,d = [],[]

        path_finder(root,start,s)
        path_finder(root,dest,d)

        while len(s) and len(d) and s[-1]==d[-1]:
            s.pop()
            d.pop()
        
        return "U"*len(s)+"".join(d[::-1])
    

arr = [5,1,2,3,-1,6,4]
    
# arr.extend([-1]*5)

startValue = 3
destValue = 6


treeNode = createTree().createTreeUsingList(arr)


# root.print_tree(treeNode)
obj = Solution()
print(obj.getDirections(treeNode,startValue,destValue))


