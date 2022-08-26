from linked_list import *


def reverse_ll(head, curr, prev):
    if curr == None:
        head = prev
        return

    forward = curr.next
    reverse_ll(head, forward, curr)
    curr.next = prev
    # return head


def reverse_with_k(head, k):
    if head == None:
        return None
    curr = head
    prev = None
    total = 0
    while total < k and curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        total += 1
    head.next = reverse_with_k(curr, k)
    return prev


if __name__ == "__main__":
    arr = [2, 3, -2, 9, 10]
    head_1 = node(arr[0])
    first = linked(head_1).create_ll(arr[1:])
    k = 3
    first1 = reverse_with_k(first, k)

    linked.printing_linked_list_external(first1)
