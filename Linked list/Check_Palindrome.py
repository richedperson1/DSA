from linked_list import *


def check_palimdrom(head):
    curr = head
    form = ""
    while curr:
        form += str(curr.data)
        curr = curr.next

    print(form == form[::-1])


def checking_palimdrom(head):
    if head.next == None:
        return True
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    while head and prev:
        if head.data != prev.data:
            return False

        head = head.next
        prev = prev.next
    return True


if __name__ == "__main__":
    linked_list = linked(None)
    arr = [1, 2]
    linked_list.create_ll(arr)
    head = linked_list.head.next

    head = checking_palimdrom(head)
    print(head)
