
from binary_tree import *
arr = [1, 2, -1, 3]
tree = createTree()
nodes = tree.createTreeUsingList(arr)


def checkHeap(head):
    if head == None:
        return True

    rootData = head.data
    if head.left and head.right:
        if rootData < head.left.data or rootData < head.right.data:
            return False
    return checkHeap(head.left) and checkHeap(head.right)


def checkHeapHeight(head):
    if head == None:
        return 0

    left = checkHeapHeight(head.left)
    right = checkHeapHeight(head.right)
    if type(left) == bool or type(right) == bool:
        return False

    if left < right or abs(left-right) > 1:
        return False
    return max(left, right)+1


root.print_tree(nodes)
condition1 = checkHeapHeight(nodes)
condition2 = checkHeap(nodes)

print(condition1)
