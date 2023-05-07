"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
"""

from linked_list import *
from collections import defaultdict

"""
Method 1
"""
def deleteDuplicates( head) :
    
    curr = node(-1)
    curr2 = curr 
    while head:
        lst = defaultdict(int)
        value = head.data
        head2 = head
        while head and head.data==value:
            head = head.next 
            lst[value]+=1
            
        if lst[value]==1:
            curr.next = head2
            curr = curr.next
            curr.next = None
            
    return curr2.next

"""
Method 2
"""

def deleteDuplicates2( head):
    heading = node(-1)
    heading2 = heading
    
    while head:
        curr = head
        flag = True
        val = 0
        while curr and curr.data==head.data:
            if val>=1:
                flag = False
            val+=1
            curr = curr.next
        
        if flag:
            heading.next = head
            # head = head.next
            heading = heading.next
            heading.next = None
            
        # else:
        head = curr
            
    return heading2.next


arr = sorted([1,2,2,2,2,3,3,3,4,4,4,4])
head = None
head2 = None
for num in arr:
    if not head:
        head = node(num)
        head2 = head
    else:
        newNode = node(num)
        head.next = newNode
        head = head.next


# deleteDuplicates(head2)
deleteDuplicates2(head2)