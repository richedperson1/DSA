from linked_list import *
"""
approach 1
T.C = O(n)
S.C = O(1)

Note : it will replace data
interviewer may ask other approach 

"""


def sort_linked(head):
    curr = head
    zero = 0
    one = 0
    two = 0
    while curr:
        if curr.data == 0:
            zero += 1
        elif curr.data == 1:
            one += 1
        else:
            two += 1

        curr = curr.next
    curr = head
    while curr:
        if zero > 0:
            zero -= 1
            curr.data = 0
        elif one > 0:
            one -= 1
            curr.data = 1
        else:
            two -= 1
            curr.data = 2
        curr = curr.next
    return head


"""
approach 1
T.C = O(n)
S.C = O(1)

Note : it will replace linked 

more optimal answer
"""


def insertAtTail(node_point, curr):
    node_point.next = curr
    node_point = curr
    return node_point


def sort_0s_1s_2s(head):
    curr = head
    zero = node("start")
    one = node("start")
    two = node("start")
    zero_t = zero
    one_t = one
    two_t = two
    while curr:
        if curr.data == 0:
            zero_t.next = curr
            zero_t = zero_t.next
        elif curr.data == 1:
            one_t.next = curr
            one_t = one_t.next
        else:
            two_t.next = curr
            two_t = two_t.next
        curr = curr.next

    if one.next == None:
        zero_t.next = two.next
    else:
        zero_t.next = one.next
    one_t.next = two.next
    two_t.next = None
    head = zero.next
    return head


if __name__ == "__main__":
    linked_list = linked(None)
    arr = [2, 1, 0]
    linked_list.create_ll(arr)
    head = linked_list.head.next
    # head_2 = sort_linked(head)
    head_3 = sort_0s_1s_2s(head)
    linked.printing_linked_list_external(head_3)
