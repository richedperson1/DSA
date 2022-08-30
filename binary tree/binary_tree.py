class root:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def print_tree(root):
        if root == None:
            return
        print(root.data, end=" : ")
        if root.left != None:
            print(" L : ", root.left.data, end=' ')
        if root.right != None:
            print(" R ", root.right.data, end="")
        print()
        root.print_tree(root.left)
        root.print_tree(root.right)


class createTree:
    def createTreeUser(rootData=None) -> root:
        rootData = int(input("Enter the value : "))
        if rootData == -1:
            return None
        rootNode = root(rootData)
        leftNode = createTree()
        rightNode = createTree()
        rootNode.left = leftNode
        rootNode.right = rightNode
        return rootNode
