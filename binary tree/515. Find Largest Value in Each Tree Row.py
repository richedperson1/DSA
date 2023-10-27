"""
! URL : https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""

# createTreeUsingList

from binary_tree import *
from collections import deque 


class Solution:
    def largestValues(self, root) -> list[int]:
        if not root:
            return []
        pq = []
        pq.append([root.val,root])
        ans = []

        while pq:
            rootAns = -float("inf")
            size = len(pq)
            for _ in range(size):
                value,rootNode = pq.pop(0)
                print(rootNode)
                # continue
                rootAns = max(rootAns,value)
                if rootNode.left and rootNode.left.val!=None:
                    pq.append([rootNode.left.val,rootNode.left])
                
                if rootNode.right and rootNode.right.val:
                    pq.append([rootNode.right.val,rootNode.right])
            ans.append(rootAns)
        return ans
    
    def largestValues1(self, root) -> list[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            current_length = len(queue)
            curr_max = float("-inf")
            
            for _ in range(current_length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(curr_max)
        
        return ans

binaryTree = createTree()

treeArr =[3,1,5,0,2,4,6,None,None,None,3]
treeArr = [3,1,5,0,2,4,None,4,6,None,None,None,3]
# treeArr =[]


rootNode = binaryTree.createTreeUsingList(treeArr)

                
obj = Solution()
print(obj.largestValues(rootNode))






            