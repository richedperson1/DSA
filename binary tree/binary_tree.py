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
    def createTreeUser(self) -> root:
        rootData = int(input("Enter the value : "))
        if rootData == -1:
            return None
        rootNode = root(rootData)
        leftNode = self.createTreeUser()
        rightNode = self.createTreeUser()
        rootNode.left = leftNode
        rootNode.right = rightNode
        return rootNode


class cloning:
    def clone(self, nodes, dist):
        if nodes == None:
            return dist
        new = root(nodes.data)
        dist[nodes] = new
        self.clone(nodes.left, dist)
        self.clone(nodes.right, dist)
        return dist

    def cloneTree(self, first, form):
        if first == None:
            return form
        item = form[first]
        item.left = form[first.left]
        item.right = form[first.right]
        self.cloneTree(first.left, form)
        self.cloneTree(first.right, form)

    def cloneWholeTree(self, fromReplication):
        cloneItem = self.clone(fromReplication, {None: None})
        self.cloneTree(fromReplication, cloneItem)
        return cloneItem[fromReplication]
