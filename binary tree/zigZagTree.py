class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result = []
        queue = [root]
        left_to_right = True

        while queue:
            level_size = len(queue)
            level = []

            for i in range(level_size):
                node = queue.pop(0)

                if left_to_right:
                    level.append(node.val)
                else:
                    level = [node.val] + level

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right

        return result
