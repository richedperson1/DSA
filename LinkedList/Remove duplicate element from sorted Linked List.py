'''
!URL : https://practice.geeksforgeeks.org/problems/remove-duplicate-element-from-sorted-linked-list/1
'''

def removeDuplicates(head):
    #code here
    if not (head):
        return head
    
    curr = head
    val = curr.data
    prev = curr
    curr = curr.next
    while curr:
        if curr.data==val:
            curr = curr.next
        
        else:
            val = curr.data
            prev.next = curr
            prev = curr
            curr = curr.next
    prev.next = None
    return head