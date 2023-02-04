from binary_tree import *


def addedInBST(Droot, k):
    if Droot == None:
        return root(k)

    if Droot.data < k:
        Droot.right = addedInBST(Droot.right, k)

    elif Droot.data > k:
        Droot.left = addedInBST(Droot.left, k)

    return Droot


def addingBST(treeNode, k):
    local = treeNode
    prev = None
    while treeNode != None:
        if treeNode.data > k:
            prev = treeNode
            treeNode = treeNode.left

        elif treeNode.data < k:
            prev = treeNode
            treeNode = treeNode.right

    if prev != None and prev.data > k:
        prev.left = root(k)
    elif prev != None and prev.data < k:
        prev.right = root(k)

    return local


treeNode = createTree().createTreeUsingList([4, 2, 7, 1, 3])
root.print_tree(treeNode)
print("---"*10)
# newTree = addedInBST(treeNode, 5)
# root.print_tree(newTree)
print("---"*10)
treeNode1 = addingBST(treeNode, 5)
root.print_tree(treeNode1)
