from binary_tree import *
import sys
treeElements = [4, 2, 8, 1, 3, 7, 10]

notBST = createTree().createTreeUsingList(treeElements)


def checkBST_min(nodes):
    if nodes == None:
        return sys.maxsize
    left = checkBST_min(nodes.left)
    right = checkBST_min(nodes.right)
    return min(left, right)


def checkBST_max(nodes):
    if nodes == None:
        return -sys.maxsize

    left = checkBST_max(nodes.left)
    right = checkBST_max(nodes.left)
    return max(left, right)


def checkBST_naive(nodes):
    if nodes == None:
        return True

    left_ = checkBST_naive(nodes.left)
    right_ = checkBST_naive(nodes.right)

    leftMax = checkBST_max(nodes.left)
    rightMin = checkBST_min(nodes.right)

    if left_ == False or right_ == False or nodes.data > leftMax or nodes.data < rightMin:
        return False
    return True


print(checkBST_naive(notBST))
root.print_tree(notBST)
