class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


first_node = binary_tree(5)
second_node = binary_tree(6)
third_node = binary_tree(4)

first_node.left = second_node
first_node.right = third_node


def print_binary_tree(root):
    if root:
        print_binary_tree(root.left)
        print(root.data)
        print_binary_tree(root.right)


def printTreeDetails(root):
    if root == None:
        return
    print(root.data, end=":")
    if root.left != None:
        print("L :----> ", root.left.data, end=',')
    if root.right != None:
        print("R :----> ", root.right.data, end="")
    print()
    printTreeDetails(root.left)
    printTreeDetails(root.right)


# print_binary_tree(first_node)
printTreeDetails(first_node)
