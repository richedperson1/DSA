"""
? URL : https://leetcode.com/problems/reverse-linked-list/
"""

"""
Time complexity : O(n)
Space complexity : O(1)
"""
def reverseList( head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev