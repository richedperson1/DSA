"""
URL : https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""

# Importing library
from binary_tree import *


class treeNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.right = right
        self.left = left


lst = [1, 2, 3, 4, 5, 6]
lst = [1, 2, 3, 4, 5, 6, 7]
lst = [-10, -3, 0, 5, 9]


def add_elemet(arr, low, high):
    if low >= high:
        return None
    mid = (low+high)//2
    newNode = treeNode(arr[mid])

    newNode.left = add_elemet(arr, low, mid)
    newNode.right = add_elemet(arr, mid+1, high)

    return newNode


new_tree = add_elemet(lst, 0, len(lst))
root.print_tree(new_tree)
