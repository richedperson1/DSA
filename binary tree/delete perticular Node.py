from binary_tree import *


def addedInBST(Droot, leftN):
    if Droot == None:
        return leftN

    if Droot.data < leftN.data:
        Droot.right = addedInBST(Droot.right, leftN)

    elif Droot.data > leftN.data:
        Droot.left = addedInBST(Droot.left, leftN)

    return Droot


def delete(nodes):

    if not(nodes.left) and nodes.right:
        return nodes.right
    elif not(nodes.right) and nodes.left:
        return nodes.left

    elif not(nodes.right) and not(nodes.left):
        return None

    else:
        return addedInBST(nodes.right, nodes.left)


def deleteNode(treeNode, k):
    if treeNode == None:
        return None

    if treeNode.data == k:
        return delete(treeNode)

    elif treeNode.data > k:
        treeNode.left = deleteNode(treeNode.left, k)
    else:
        treeNode.right = deleteNode(treeNode.right, k)

    return treeNode


lst = [5, 3, 6, 2, 4, 5.5, 7]
deleteTree = createTree().createTreeUsingList(lst)

root.print_tree(deleteTree)

print("--"*10)
new = deleteNode(deleteTree, 5)
root.print_tree(new)
