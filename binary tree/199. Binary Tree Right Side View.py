from collections import deque
class Solution:
    def rightSideView(self, root) -> list[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while len(queue)>0:
            size = len(queue)
            rightside = None
            for ind in range(size):
                node = queue.popleft()
                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightside:
                ans.append(rightside.val)
        return ans