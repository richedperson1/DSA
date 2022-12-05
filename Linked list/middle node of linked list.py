"""
URL : https://leetcode.com/problems/middle-of-the-linked-list/
"""

"""
Time complexity : O(n)
space complexity : O(1)

"""


def middleNodeUsingCount(head):
    num = 0
    curr = head
    while curr:
        curr = curr.next
        num += 1

    curr = head
    for _ in range(num//2):
        curr = curr.next

    return curr


"""
Time complexity : O(n)
space complexity : O(1)

"""


def middleNode2Pointer(head):
    # Using two pointer approach
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
