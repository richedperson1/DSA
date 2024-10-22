from collections import deque
from binary_tree import *
class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        
        first,second = 0 ,0

        stack = deque([])

        stack.append((1,root))

        level_wise = []

        while len(stack):
            size = len(stack)
            total = 0
            for _ in range(size):
                level,node = stack.popleft()
                total+=node.val
                if node.left:
                    stack.append((level+1,node.left))
                if node.right:
                    stack.append((level+1,node.right))
            
            level_wise.append([total,level])
        print(level_wise)
        if len(level_wise)<k:
            return []
        return(sorted(level_wise,reverse=True)[k-1])[0]
    

arr = [5,8,9,2,1,3,7,4,6]
arr = [5,8,9,2,1,3,7]
k = 4
tree = createTree().createTreeUsingList(arr)

obj = Solution()

print(obj.kthLargestLevelSum(tree,k))