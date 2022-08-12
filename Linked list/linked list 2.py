class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self, head):
        self.head = head

    def printing(self):
        if self.head.next is None:
            print("Linked list is empty")
            return "Linked list is empty"

        iterator = head.next
        while iterator.next:
            print(iterator.data, " --->", end=' ')
            iterator = iterator.next
        print(iterator.data)

    def insert(self, data):
        while self.head.next:
            self.head = self.head.next

        if type(data) == list:
            for i in data:
                self.head.next = node(i, None)
                self.head = self.head.next


head = node()
obj = linked_list(head)
# obj.printing()
lst = [i for i in range(10)]
obj.insert(lst)

obj.printing()
