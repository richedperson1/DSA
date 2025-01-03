from collections import deque
from binary_tree import *
class Solution:
    def replaceValueInTree(self, root) :
        if not root:
            return []
        stack = deque()
        total = 0
        if root.left:
            stack.append((root,root.left))
            total+=root.left.val
        if root.right:
            total+=root.right.val
            stack.append((root,root.right))
        
        root.val = 0
        while len(stack):
            size = len(stack)
            total2 = 0
            for _ in range(size):
                parent,node = stack.popleft()
                local_weight = 0
                if parent.left:
                    local_weight += parent.left.val
                if parent.right:
                    local_weight+= parent.right.val

                if total-local_weight<=0:
                    node.val = 0
                    # ans.append(0)
                else:
                    node.val = total-local_weight
                    # ans.append(total-local_weight)
                
                if node.left:
                    total2 += node.left.val
                    stack.append((node,node.left))
                if node.right:
                    total2 += node.right.val
                    stack.append((node,node.right))
            
            total = total2
        return root
    
null = -1
arr = [5,4,9,1,10,null,7]

tree = createTree().createTreeUsingList(arr)
obj = Solution()
root.print_tree(tree)
root.print_tree(nodes=obj.replaceValueInTree(root=tree))

