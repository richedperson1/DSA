
"""
! URL : https://practice.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1
"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None
def addNode(head, p, data):
    curr = head
    prev = None
    for ind in range(p):
        head = head.next
    
    newNode = Node(data)
    newNode.prev = head
    
    headNxt = head.next
    head.next = newNode
    
    newNode.next = headNxt
    if headNxt:
        headNxt.prev = newNode
        
    return curr