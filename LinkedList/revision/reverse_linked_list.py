

import sys
import os

# Add the path of the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now, you can import extensions.py

from linked_list import *

obj = linked(None)

# lList  = obj.create_ll([1,2,3,4,5,6,7,8,9])
lList  = obj.create_ll([1,2,3])

def reverse_linked_list_recursive(head):
    if head ==None or head.next==None:
        return head,head
    
    nxt,first = reverse_linked_list_recursive(head.next)
    
    nxt.next = head
    head.next = None
    return head,first

reverse_list,head = reverse_linked_list_recursive(lList)
obj.printing_linked_list_external(head)