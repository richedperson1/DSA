from collections import deque
class Solution:
    def connect(self, root) :

        stack = deque([(root,0)])
        prev = None
        curr = root
        prevLevel = None
        while len(stack)>0:
            new_data = stack.popleft()
            print(new_data)
            node,level = new_data
            if not prev and not prevLevel:
                prev = node
                prevLevel = level
            elif prevLevel==level:
                prev.next = node
                prev = node
            else:
                prevLevel = level
                prev = node
            
            if node and node.left:
                stack.append((node.left,level+1))
            if node and node.right:
                stack.append((node.right,level+1))

        return root
