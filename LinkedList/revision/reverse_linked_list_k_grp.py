from LinkedList.linked_list import *


obj = linked()

lList  = obj.create_ll([1,2,3,4,5,6,7,8,9])


def reverseLinkList(head,k):

    def reverse_k_grp(head):
        if not head:
            return head
        
        total = 0
        prev = None
        curr = head
        while head and total<k :
            nxt = head.next
            
            head.next = prev
            prev = head
            head = nxt
            total+=1
            
        curr.next = reverse_k_grp(prev)
        return prev
    
    return reverse_k_grp(head)


obj.printing_linked_list_external(reverseLinkList(lList))