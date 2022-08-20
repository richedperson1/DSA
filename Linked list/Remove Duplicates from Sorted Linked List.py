def uniqueSortedList(head):
    # write your code here
    curr = head
    while head:
        if head.next and head.data == head.next.data:
            local = head
            while local.next and local.data == local.next.data:
                local = local.next
            head.next = local.next
        head = head.next
    return curr
