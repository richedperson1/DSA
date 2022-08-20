from linked_list import *


def is_circular(head):
    if head == None:
        return True
    if head.next == None:
        return False
    fast = head.next.next
    slow = head.next
    while fast != None and fast.next != None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False


if __name__ == "__main__":
    head = None
    obj = linked(head)
    arr = [1, 2, 3, 4, 5]
    k = 2
    obj.create_ll(arr)
    head = obj.head.next

    is_true = is_circular(head)
    print(is_true)
