from linked_list import *


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def detect_circle(head):
    fast = head.next.next
    slow = head.next
    while fast and fast.next != None:
        if slow == fast:
            return fast
        fast = fast.next.next
        slow = slow.next
    return False


def removeLoop(head: Node) -> Node:

    # Write your code
    modifiend = head
    curr = head
    if head == None or head.next == None:
        return head
    fast = detect_circle(curr)
    if fast == False:
        return modifiend
    slow = head
    while fast.next != slow.next:
        fast = fast.next
        slow = slow.next
    if fast.next == slow.next:
        fast.next = None
    return head


if __name__ == "__main__":
    head = None
    obj = linked(head)
    arr = list(map(int, "893 166 16 729 551 296 361 478 304 301 920 676 675 828 324 888 959 409 548 785 377 317 824 121 596 677 779 863 929 433 206 555 906 705 184 749 47 417 415 683".split()))
    k = 2
    obj.create_ll(arr)
    head = obj.head.next

    is_true = removeLoop(head)
    linked.printing_linked_list_external(is_true)
    print("Time Loop is ended  ------> 🤗")
