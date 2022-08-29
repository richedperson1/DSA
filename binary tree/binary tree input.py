from binary_tree import root as root_node


def user_tree_create(root, arr, i):
    if i == len(arr):
        return root
    if root.left and root.right:
        user_tree_create(root.left, arr, i)
    elif root.right:
        root.left = root_node(arr[i])
        user_tree_create(root, arr, i+1)
    else:
        root.right = root_node(arr[i])
        user_tree_create(root, arr, i+1)


root = root_node(0)
lsr = [2, 3, 4, 5]
rooting = user_tree_create(root, lsr, 0)
root_node.print_tree(root)
