"""
URL : https://leetcode.com/problems/reorder-list/
"""
from linked_list import *
from collections import defaultdict
import math
arr = [1, 2, 3, 4, 5]


def linkedListReorder(head):
    final = defaultdict()
    curr = head
    ind = 0
    while curr:
        final[ind] = curr
        curr = curr.next
        ind += 1

    n = len(final)-1
    if n <= 1:
        return head
    ind = 0
    final[ind] = False
    ind += 1

    curr = head
    curr2 = curr
    curr.next = final[n]
    curr = curr.next
    final[n] = False
    n -= 1
    while True:
        if final[ind] != False:
            first = final[ind]
            second = final[n]

            curr.next = first
            curr = curr.next

            curr.next = second
            curr = curr.next
            final[n] = False
            final[ind] = False
            n -= 1
            ind += 1
        else:
            break

    curr.next = None
    return curr2


linked_list = linked(None)
linked_list.create_ll(arr)


linkedList = linked_list.head.next
new_key = linkedListReorder(linkedList)
while new_key:
    print(new_key.data)
    new_key = new_key.next
