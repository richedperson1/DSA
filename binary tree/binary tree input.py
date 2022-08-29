from binary_tree import root as root_node


def user_tree_create(root, arr, i):
    if i == len(arr):
        return root
    if root.left and root.right:
        user_tree_create(root.left, arr, i)
        # user_tree_create(root.right, arr, i+2)
    elif root.right:
        root.left = root_node(arr[i])
        user_tree_create(root, arr, i+1)
    else:
        root.right = root_node(arr[i])
        user_tree_create(root, arr, i+1)


def createTree() -> root_node:
    rootData = int(input("Enter the value : "))
    if rootData <= -1:
        return None
    root = root_node(rootData)
    leftNode = createTree()
    rightNode = createTree()
    root.left = leftNode
    root.right = rightNode
    return root


root = root_node(0)
lsr = [2, 3, 4, 5, 9, 6]
rooting = user_tree_create(root, lsr, 0)
root_node.print_tree(root)

# head_node = createTree()
# root_node.print_tree(head_node)
