from binary_tree import *

arr = [10, 5, 15, 3, 7, -1, 18]
rootNode = createTree().createTreeUsingList(arr)


def rangeSum(nodes, low, high):
    if nodes == None:
        return 0

    ans = 0
    if nodes.data >= low and nodes.data <= high:
        ans += nodes.data
        ans += rangeSum(nodes.left, low, high)
        ans += rangeSum(nodes.right, low, high)

    elif nodes.data < low:
        ans += rangeSum(nodes.right, low, high)

    elif nodes.data > high:
        ans += rangeSum(nodes.left, low, high)

    return ans


low, high = 7, 15
print(rangeSum(rootNode, low, high))
