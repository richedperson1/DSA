"""
URL : https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List
class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def bfs(node):
            stack = [(node,0)]
            while stack:
                node,pos = stack.pop()
                if len(ans)>= (pos+1):
                    ans[pos].append(node.val)
                else:
                    ans.append([])
                    ans[-1].append(node.val)
                
                if node.right:
                    stack.append((node.right,pos+1))
                if node.left:
                    stack.append((node.left,pos+1))
        
        bfs(root)
        return ans