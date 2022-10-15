from binary_tree import *

arr = [5, 3, 10, 1, 4, 6, 12]

bst = createTree().createTreeUsingList(arr)
root.print_tree(bst)


def bstToHeap(head, arr):
    if head == None:
        return arr

    arr = bstToHeap(head.left, arr)
    arr.append(head.data)
    arr = bstToHeap(head.right, arr)
    return arr


arr = bstToHeap(bst, [])

i = 0


# def convertBST2Heap(roots, arr):
#     global i
#     if roots == None or i >= len(arr):
#         return roots
#     roots.data = arr[i]
#     i += 1
#     convertBST2Heap(roots.left, arr)
#     convertBST2Heap(roots.right, arr)
#     return roots


# # print(arr)
# newOne = convertBST2Heap(bst, arr)
# # print(newTree)
# print("* * "*20)
# root.print_tree(newOne)
