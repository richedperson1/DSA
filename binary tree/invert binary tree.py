def invertTree(self, root):
    if not root:
        return

    temp = root.left
    root.left = root.right
    root.right = temp
    self.invertTree(root.right)
    self.invertTree(root.left)
    return root
