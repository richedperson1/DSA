from collections import deque
# The code is implementing a diagonal traversal of a binary tree.
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
    
        if not root:
            return []
            
        node = deque()
        node.append(root)
        ans = []
        while len(node)>0:
            temp = node.popleft()
            while temp is not None :
                if temp:
                    ans.append(temp.data)
                if temp.left:
                    node.append(temp.left)
                    
                temp = temp.right

        return ans