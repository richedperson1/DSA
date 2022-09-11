from binary_tree import *
import sys
treeElements = [4, 3, 8, 1, 3, 7, 10]

notBST = createTree().createTreeUsingList(treeElements)


def checkBST_min(nodes):
    if nodes == None:
        return sys.maxsize
    left = checkBST_min(nodes.left)
    right = checkBST_min(nodes.right)
    return min(left, right, nodes.data)


def checkBST_max(nodes):
    if nodes == None:
        return -sys.maxsize

    left = checkBST_max(nodes.left)
    right = checkBST_max(nodes.right)
    return max(left, right, nodes.data)


def checkBST_naive(nodes):
    if nodes == None:
        return True

    leftMax = checkBST_max(nodes.left)
    rightMin = checkBST_min(nodes.right)

    if nodes.data < leftMax or nodes.data > rightMin:
        return False

    left_ = checkBST_naive(nodes.left)
    right_ = checkBST_naive(nodes.right)
    return left_ and right_


print(checkBST_naive(notBST))
root.print_tree(notBST)
