from binary_tree import *

lst = list(map(int, "5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1".split()))

binaryTree = createTree().createTreeUsingList(8, lst)


def search(nodes, k):
    if nodes == None:
        return nodes
    if nodes.data == k:
        return nodes
    elif nodes.data > k:
        return search(nodes.left, k)
    else:
        return search(nodes.right, k)


a = search(binaryTree, 5)
print(a.data)
print(a)
