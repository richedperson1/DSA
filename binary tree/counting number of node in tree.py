from binary_tree import root as root_node


def user_tree_create(root, arr, i=0):
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


def count_node(root, count):
    if root == None:
        return count
    if root.left == None and root.right == None:
        count += 1
        return count
    count = count_node(root.left, count)
    count = count_node(root.right, count)
    return count


if __name__ == "__main__":
    lst = [2, 3, 4, 5, 6, 7, 8]
    first_node = root_node(1)
    form_tree = user_tree_create(first_node, arr=lst)
    # formTree = createTree()
    root_node.print_tree(first_node)
    print(count_node(first_node, 0))
