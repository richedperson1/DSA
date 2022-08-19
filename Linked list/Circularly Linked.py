from linked_list import *


if __name__ == "__main__":
    head = None
    obj = linked(head)
    arr = [1, 2, 3, 4, 5]
    k = 2
    obj.create_ll(arr)
    head = obj.head.next
    reverse_head = reverseKGroup(head, k)
    linked.printing_linked_list_external(reverse_head)
