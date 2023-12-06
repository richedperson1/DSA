"""
! URL : https://practice.geeksforgeeks.org/problems/sort-a-linked-list/1
"""

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if not(head and head.next):
            return head
        
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left = slow.next
        slow.next = None
        left = self.mergeSort(left)
        right = self.mergeSort(head)
        
        temp = Node("start")
        current = temp
        
        while left and right:
            if left.data>right.data:
                current.next = right
                right = right.next
            else:
                current.next = left
                left = left.next
            
            current = current.next
        
        current.next = left or right
        
        return temp.next