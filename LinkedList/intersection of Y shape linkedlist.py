
def findIntercept(head1,head2):
    while head2  and  head1  and  head1!=head2:
        head1 = head1.next
        head2 = head2.next
    
    first = head1.data if head1 else -1
    while head2  and  head1  and  head1==head2:
        head1 = head1.next
        head2 = head2.next
    
    
    return first

def intersetPoint(head1,head2):
    size1 = 0
    size2 = 0
    c1,c2 = head1,head2
    while head1:
        size1+=1
        head1 = head1.next
    
    while head2:
        size2+=1
        head2 = head2.next
        
    head1,head2 = c1,c2
    diff = abs(size1-size2)
    if diff==0:
        return findIntercept(head1,head2)
    else:
        if head1  and  size1>size2:
            while size1!=size2:
                size1-=1
                head1 = head1.next
            return findIntercept(head1,head2)
            
        else:
            while head2  and  size1!=size2:
                size2-=1
                head2 = head2.next
            return findIntercept(head1,head2)

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data
    def __str__(self):
        return self.data
class LinkedList:
    def __init__(self):
        self.head = None
        temp=None
    def __repr__(self):
        return self.head
    def __str__(self):
        return self.head
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next

if __name__ == '__main__':
    t=1
    for cases in range(t):
        # x,y,z = map(int,input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int,"1 2 6".strip().split()))
        nodes_b = list(map(int, "1 6 6".strip().split()))
        nodes_common = list(map(int, "7 8".strip().split()))
        # nodes_common = []

        for x in nodes_a:
            node=Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node=Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node=Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i== 0:
                b.append(node)  # add to the end of the list b, only the intersection
        
        print(intersetPoint(a.head,b.head))

# } Driver Code Ends