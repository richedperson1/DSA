
import sys
import os

# Add the path of the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now, you can import extensions.py

from linked_list import *

obj = linked(None)

lList  = obj.create_ll([1,2,3,4,5,6,7,8,9])


def reverseLinkList(head,k):

    def reverse_k_grp(head):
        if not head:
            return head
        
        total = 0
        prev = None
        curr = head
        while head and total<k :
            nxt = head.next
            
            head.next = prev
            prev = head
            head = nxt
            total+=1
            
        curr.next = reverse_k_grp(head)
        return prev
    
    return reverse_k_grp(head)

obj.printing_linked_list(reverseLinkList(lList,3))
