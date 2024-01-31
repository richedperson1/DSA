

class Solution:
    def preorderTraversal(self, root) -> list[int]:
        ans = []
        def bfs(node):
            if not node:
                return node
            
            curr = node
            stack = []
            res = []
            while curr or stack:
                while curr:
                    res.append(curr.val)
                    curr = curr.left
                    stack.append(curr.right)
                
                curr = stack.pop()
            
        bfs(root)
        return ans