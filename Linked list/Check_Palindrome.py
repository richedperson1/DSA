from linked_list import *


def check_palimdrom(head):
    curr = head
    form = ""
    while curr:
        form += str(curr.data)
        curr = curr.next

    print(form == form[::-1])


if __name__ == "__main__":
    linked_list = linked(None)
    arr = [2, 1, 2]
    linked_list.create_ll(arr)
    head = linked_list.head.next
    check_palimdrom(head)
