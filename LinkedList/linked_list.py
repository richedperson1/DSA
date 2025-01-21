class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)


class linked:
    def __init__(self, head=None):
        if head == None:
            self.head = None
        else:
            self.head = head

    def add_element(self, ele):

        self.tail = 0
        curr = self.head
        while curr.next:
            curr = curr.next

        new = node(ele)
        curr.next = new
        self.tail = new

    def add_node(self, node):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    def create_ll(self, arr=[2, 4, 5, 6, 8, 9]):
        flag = False

        if self.head == None:
            first_node = node(arr[0])
            if len(arr)==1:
                return first_node
            flag = True
            curr = first_node
            self.head = curr
        else:
            flag = False
            curr = self.head
        while curr.next:
            curr = curr.next
        if flag:
            for ind, num in enumerate(arr):
                if ind == 0:
                    continue
                new = node(num)
                # print(curr)
                curr.next = new
                curr = new
        else:
            for num in arr:
                new = node(num)
                curr.next = new
                curr = new
        
        self.tail = new
        return self.head

    def printing_linked_list(self,head=None):
        """
        This function printing linked list elements

        """
        # print(self.head,head)
        curr = self.head if not head else head
        while curr is not None:
            if curr.next is None:
                print(curr.data, end="")
            else:
                print(curr.data, end=' ----> ')
            curr = curr.next
        print('')

    def printing_linked_list_external(self,head):
        """
        This function printing linked list elements

        """
        curr = head
        while curr != None:
            if curr.next is None:
                print(curr.data, end="")
            else:
                print(curr.data, end=' ----> ')
            curr = curr.next
        print('')

    def printing_circular_linked_list_external(self,head):
        """
        This function printing linked list elements

        """
        curr = head
        while curr.next != head:
            print(curr.data, end=" ---> ")
            curr = curr.next

        print(curr.data)
