
from binary_tree import *


def checkValidBST(nodes, left, right):
    if nodes == None:
        return True

    if nodes.data < left or nodes.data > right:
        return False

    leftV = checkValidBST(nodes.left, left, nodes.data-1)
    rightV = checkValidBST(nodes.right, nodes.data, right)

    return leftV and rightV


Max = 2**32
tree = [1, -1, 1]

notBST = createTree().createTreeUsingList(tree)
# root.print_tree(notBST)

print(checkValidBST(notBST, -Max, Max))
