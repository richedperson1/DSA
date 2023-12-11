
from linked_list import *

class Solution:
    def compute(self,head):
        #Your code here
        if not (head and head.next):
            return head
            
        curr = head
        prev = None
        while curr:
            curr.prev = prev
            prev = curr
            curr = curr.next
            
        
        curr = prev
        maxi = 0
        nxt = None
        
        while curr:
            if curr.data<maxi:
                curr = curr.prev
                continue
            
            maxi = max(maxi,curr.data)
            curr.next = nxt
            nxt = curr
            curr = curr.prev
        return nxt
    


ll_arr = linked()
ll_arr.create_ll([2,3,5,6,1,2])
ll_arr.printing_linked_list()

print(ll_arr.head)

obj = Solution()
ll_arr.printing_linked_list(obj.compute(ll_arr.head))
# print(obj.compute(ll_arr.head))