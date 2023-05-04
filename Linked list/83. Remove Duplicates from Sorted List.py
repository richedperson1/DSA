from linked_list import *

def deleteDuplicates( head):
    
    curr = head
    curr1 = curr
    while head:
        currVal = curr.val
        while head and head.val==currVal:
            head = head.next
            
        curr.next = head
        curr = curr.next
        if head:
            head = head.next
    return curr1


