from linked_list import node as Node,linked
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        new_node = Node(-1)
        start = new_node
        while head1 and head2:
            if head1.data>head2.data:
                new_node.next = head2
                new_node = head2
                head2 = head2.next
            else:
                new_node.next = head1
                new_node = head1
                head1 = head1.next
                
        while head1:
            new_node.next = head1
            new_node = head1
            head1 = head1.next
          
        while head2:
            new_node.next = head2
            new_node = head2
            head2 = head2.next  
        new_node.next = None
        
        return start.next
    

arr = [5,10,15,40]
brr = [2,3,20]

linked_obj = linked()
arr_ll = linked().create_ll(arr)
brr_ll = linked().create_ll(brr)

linked_obj.printing_linked_list(arr_ll)
linked_obj.printing_linked_list(brr_ll)
obj = Solution().sortedMerge(arr_ll,brr_ll)

linked_obj.printing_linked_list(obj)
