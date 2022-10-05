from binary_tree import *

from binary_tree import *
arr = [8, 7, 6, -1, -1, 5, 4]
tree = createTree()
nodes = tree.createTreeUsingList(arr)


def isHeap(root):
    if root == None or not(root.left) or not(root.right):
        return True
    if not(root.left) or not(root.right):
        return True

    left = isHeap(root.left)
    right = isHeap(root.right)

    rootData = root.data

    if left == False or right == False:
        return False
    elif root.left and root.right and (rootData > root.left.data and rootData > root.right.data):
        return True
    elif root.left and not(root.right) and rootData > root.left.data:
        return True
    elif root.right and not(root.left) and rootData > root.right.data:
        return True
    else:
        return False


print(isHeap(nodes))
