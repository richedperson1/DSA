class root:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self, root):
        if root == None:
            return
        print(root.data, end=" : ")
        if root.left != None:
            print(" L : ", root.left.data, end=' ')
        if root.right != None:
            print(" R ", root.right.data, end="")
        print()
        self.print_tree(root.left)
        self.print_tree(root.right)
