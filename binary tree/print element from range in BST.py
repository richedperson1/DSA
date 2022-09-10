from binary_tree import *

lst = list(map(int, "5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1".split()))

binaryTree = createTree().createTreeUsingList(8, lst)

root.print_tree(binaryTree)


def printRangeElements(nodes, r1, r2):
    if nodes == None:
        return
    if nodes.data > r1:
        printRangeElements(nodes.left, r1, r2)

    if nodes.data < r2:
        printRangeElements(nodes.right, r1, r2)

    if nodes.data >= r1 and nodes.data <= r2:
        print(nodes.data, end=" ----> ")


printRangeElements(binaryTree, 6, 15)
