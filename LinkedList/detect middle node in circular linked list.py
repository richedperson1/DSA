from linked_list import *


def middle_node(head):
    curr = head
    total = 0
    tail = None
    while curr.next != head:
        total += 1
        curr = curr.next

    tail = curr
    curr = head
    middle = None
    next1 = None

    for i in range(total):

        if i == (total//2):
            middle = curr
            next1 = curr.next
            break
        curr = curr.next

    middle.next = head
    tail.next = next1
    return [head, next1]


if __name__ == "__main__":
    linked_list = linked(None)
    arr = [2, 3, 4, 5, 3]
    linked_list.create_ll(arr)
    tail = linked_list.tail
    head = linked_list.head.next
    tail.next = head
    left, right = middle_node(head)
    linked.printing_circular_linked_list_external(left)
