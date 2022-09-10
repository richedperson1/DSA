from binary_tree import *
arr = [-10, -3, 0, 5, 9]


def middle_index(arr):
    num = len(arr)
    return num//2
    # if num & 1:
    #     return num//2
    # return (num//2)-1


def createBST(arr, nodes=None):
    if len(arr) == 1:
        return root(arr[0])
    if len(arr) == 0:
        return None

    middle = middle_index(arr)
    rootNodes = root(arr[middle])
    rootNodes.left = createBST(arr[:middle], rootNodes)
    rootNodes.right = createBST(arr[middle+1:], rootNodes)
    return rootNodes


binaryTree = createBST(arr)
root.print_tree(binaryTree)
