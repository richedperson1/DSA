"""
URL : https://leetcode.com/problems/odd-even-linked-list/description/
"""


def oddEvenList(head):
    if head == None or head.next == None:
        return head

    odd = head
    even = head.next
    oddH = odd
    evenH = even
    if even.next == None:
        return head

    curr = even.next
    num = 3
    while curr:
        if num & 1:
            odd.next = curr
            odd = curr
        else:
            even.next = curr
            even = curr
        num += 1
        curr = curr.next

    even.next = None
    odd.next = evenH
    return oddH
