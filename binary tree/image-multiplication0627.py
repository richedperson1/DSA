from collections import deque
import math
from binary_tree import *

class Solution:
    # your task is to complete this function
    def imgMultiply(self, root):
        
        stack = deque([root])
        ans = 0
        start = True
        while len(stack)>0:
            if start:
                ans = root.data**2
                start = False
                
                root = stack.pop()
                stack.append(root.left)
                stack.append(root.right)
                continue
            
            # node_data = []
            size = len(stack)
            
            for ind in range(size):
                if len(stack)>1:
                    first = stack.popleft()
                    second = stack.pop()
                    
                    if first and second:
                        print(first,second)
                        ans+= (first.data*second.data)
                        stack.append(first.left)
                        stack.append(first.right)
                        stack.append(second.left)
                        stack.append(second.right)           
                    
        return ans
    # your task is to complete this function
        
    def imgMultiply2(self, root):
        # Code here
        res = root.data**2
        
        if root.left and root.right:
            res += root.left.data*root.right.data
            stack = deque([root.left,root.right])
            
            while len(stack)>0:
                n1 = stack.popleft()
                n2 = stack.popleft()
                
                
                if n1.left and n2.right:
                    print(n1,n2)
                    stack.append(n1.left)
                    stack.append(n2.right)
                    res += (n1.left.data*n2.right.data)
                if n1.right and n2.left:
                    print(n1,n2)
                    stack.append(n1.right)
                    stack.append(n2.left)
                    res += (n2.left.data*n1.right.data)
                    
        return res%(10**9+7)
        return ans
    
    
treeObj = createTree()
arr = list(map(int,"1 2 3 -1 4 5 6 7 -1 8 9 10 11 12 13 14 15 16 -1".split()))

tree = treeObj.createTreeUsingList(arr)
# root.print_tree(tree)

solution = Solution().imgMultiply2(tree)
print(solution)