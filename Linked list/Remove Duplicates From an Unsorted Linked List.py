from linked_list import *


def removeDuplicates(head):
    curr = head
    dist = {curr.data: True}
    while curr and curr.next:

        if curr.next and curr.next.data in dist:
            curr.next = curr.next.next
        else:
            dist[curr.data] = True
            curr = curr.next

    return head


if __name__ == "__main__":
    lst = list(map(int, ("3 2 3 4 2 3").split()))
    # print(lst)
    head = None
    obj = linked(head)
    obj.create_ll(lst)
    head = obj.head.next
    obj_head = removeDuplicates(head)
    linked.printing_linked_list_external(obj_head)
