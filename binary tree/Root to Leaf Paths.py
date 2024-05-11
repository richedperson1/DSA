from typing  import *
from binary_tree import *
class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        self.result = []
        
        def dfs(root,local):
            
            if not root:
                # self.result.append(local)
                return 
            
            if not(root.left or root.right):
                local.append(root.data)
                self.result.append(local)
                return
            dfs(root.left,local+[root.data])
            dfs(root.right,local+[root.data])
        
        dfs(root,[])
        print(self.result)
        


arr = [1,2,3]
arr = [1,2,3,4,5,-1,-1,-1,-1]
arr =list(map( int,"6 -1 4 8 5 10 3 9 11 2 7 1".split()))
arr.extend([-1]*20)
treeNode = createTree().createTreeUsingList(arr)
obj = Solution()
obj.Paths(treeNode)

root.print_tree(treeNode)