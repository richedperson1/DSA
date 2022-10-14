from binary_tree import *

arr = [5, 3, 10, 1, 2, 6, 153]

bst = createTree().createTreeUsingList(arr)
root.print_tree(bst)


def bstToHeap(head, arr):
    if head == None:
        return arr

    arr = bstToHeap(head.left, arr)
    arr.append(head.data)
    arr = bstToHeap(head.right, arr)
    return arr


print(bstToHeap(bst, []))
