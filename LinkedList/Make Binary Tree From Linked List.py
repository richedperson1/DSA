from collections import deque
from linked_list import *

# Tree Node structure
class Tree:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
obj = linked()

arr = [1,2,3,4,5,6]
linkedList = obj.create_ll(arr)

#Function to make binary tree from linked list.
def convert(head):
    treeNode = Tree(head.data)
    head = head.next
    stack = deque([treeNode])
    rootNode = treeNode
    while len(stack) and head:
        
        treeNode = stack.popleft()
        
        first = head.data
        treeNode.left = Tree(first)
        stack.append(treeNode.left)
        
        if head.next:
            second = head.next.data
            treeNode.right = Tree(second)
            stack.append(treeNode.right)
        
            head = head.next.next
        else:
            head = head.next
        
    return rootNode



print(convert(linkedList))