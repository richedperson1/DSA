from binary_tree import *


def counting(root):
    if root == None:
        return 0
    left = counting(root.left)
    right = counting(root.right)
    return 1+left+right


treeNode = createTree().createTreeUser()
# if __name__ == "__main__":
# print(counting(treeNode))
