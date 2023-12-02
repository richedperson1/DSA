
from linked_list import *


# def reverseKGroup(head, k):
#     curr = head
#     for _ in range(k):
#         if not curr:
#             return head
#         curr = curr.next
#     prev = None
#     curr = head
#     for _ in range(k):
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     head.next = reverseKGroup(curr, k)
#     return prev
def reverseKGroup(head, k):
    if head == None:
        return head
    curr = head
    prev = None
    total = 0
    while total < k and curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        total += 1
    head.next = reverseKGroup(curr, k)
    return prev


if __name__ == "__main__":
    head = None
    obj = linked(head)
    arr = [1, 2, 3, 4, 5]
    k = 2
    obj.create_ll(arr)
    head = obj.head.next
    reverse_head = reverseKGroup(head, k)
    linked.printing_linked_list_external(reverse_head)
