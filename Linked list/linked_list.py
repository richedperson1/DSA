class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)


class linked:
    def __init__(self, head):
        if head == None:
            self.head = node("start")
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
            flag = True
            curr = first_node
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
                curr.next = new
                curr = new
        else:
            for num in arr:
                new = node(num)
                curr.next = new
                curr = new
        self.tail = curr
        return self.head

    def printing_linked_list(self):
        """
        This function printing linked list elements

        """
        curr = self.head
        while curr is not None:
            if curr.next is None:
                print(curr.data, end="")
            else:
                print(curr.data, end=' ----> ')
            curr = curr.next
        print('')

    def printing_linked_list_external(head):
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
