"""
Given a linked list of N nodes. The task is to reverse this list.

Example 1:

Input:
LinkedList: 1->2->3->4->5->6
Output: 6 5 4 3 2 1
Explanation: After reversing the list, 
elements are 6->5->4->3->2->1.

[2, 4, 5, 6, 8, 9])
"""
from linked_list import linked


class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return self.data


def reverse_ll(head):
    perv = None
    cur = head
    nxt = head.next

    while cur != None:
        nxt = cur.next
        cur.next = perv
        perv = cur
        cur = nxt
    head = perv

    while head.next:
        print(head.data, end=" -----> ")
        head = head.next
    print(head.data)


def reverse_ll_recur(head, prev):
    if head == None:
        head = prev
        return head
    next = head.next
    head.next = prev
    prev = head
    head = next
    return reverse_ll_recur(head, prev)

def reverse_linked_list_recursive(head):
    if head ==None or head.next==None:
        return head
    
    nxt = reverse_linked_list_recursive(head.next)
    
    nxt.next = head
    head.next = None
    return head

def reverse_ll_recursion(head):
    return reverse_ll_recur(head, prev=None)


if __name__ == "__main__":
    head = None
    link_obj = linked(head)
    link_obj.create_ll()
    link_obj.printing_linked_list()
    head = link_obj.head
    obj = reverse_ll_recursion(head)
    linked.printing_linked_list_external(obj)
