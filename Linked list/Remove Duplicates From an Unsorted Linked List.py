from linked_list import *

"""
Remove duplicate from the linked list 
Time Complexity : O(n^2)
Space Complexity : O(1)
"""


def remove_duplicate(head):
    curr = head
    while curr.next:
        local = curr
        while local and local.next:
            if local.next.data == curr.data:
                temp = local.next
                local.next = temp.next
            else:
                local = local.next
        curr = curr.next
    return head


"""
More rigid code 
Time and space complexity is same as above

"""


def remove_duplicate_2(head):
    curr = head
    while curr.next:
        local = curr
        while local and local.next:
            if local.next.data == curr.data:
                local_3 = local.next
                while local_3 and local_3.data == curr.data:
                    local_3 = local_3.next
                local.next = local_3
            else:
                local = local.next
        curr = curr.next
    return head


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
    lst = list(map(int, ("3 3 3 3 1 3 3 ").split()))
    head = None
    obj = linked(head)
    obj.create_ll(lst)
    head = obj.head.next
    head2 = head
    obj_head_1 = remove_duplicate_2(head)
    linked.printing_linked_list_external(obj_head_1)

    # obj_head_2 = removeDuplicates(head)
    # linked.printing_linked_list_external(obj_head_2)

    # obj_head_3 = remove_duplicate(head)
    # linked.printing_linked_list_external(obj_head_3)
