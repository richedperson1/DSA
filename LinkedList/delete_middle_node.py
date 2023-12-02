from linked_list import *


def delete_middle(head):
    if head == None:
        return head
    elif head.next == None:
        return head
    fast = head.next.next
    slow = head.next
    while fast != None and slow.next != None:
        if fast.next == None:
            return slow.next.data
        slow = slow.next
        fast = fast.next.next
    return slow.data


def find_middle(head):
    total = 0
    curr = head

    while curr != None:
        total += 1
        curr = curr.next

    want = total//2
    i = 0
    if total & 1:
        want += 1
    curr = head
    while i < want:
        curr = curr.next
        i += 1
    return curr.data


if __name__ == "__main__":
    head = None
    obj = linked(head)
    arr = [1, 2, 3, 4, 5]
    obj.create_ll(arr)
    head_obj = obj.head
    print(delete_middle(head_obj))
    print(find_middle(head_obj))
