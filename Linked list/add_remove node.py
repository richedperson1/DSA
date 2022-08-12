

class node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


def linked_list_add(arr, i):
    if i == (len(arr)-1):
        return node(arr[i], None)

    node_of_link = linked_list_add(arr, i+1)
    head = node(arr[i], node_of_link)
    return head


class linked_list:
    def __init__(self, head):
        self.head = head

    def printing_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return 'Linked list is empty'

        while self.head.next != None:
            print(self.head.data, end=" ---> ")
            self.head = self.head.next
        print(self.head.data)


def adding_at_index(head, data, i):
    local = 0
    while head.next != None:
        local += 1
        if local == i:
            add = head.next
            new = node(data, add)
            head.next = new
        else:
            head = head.next


def remove_at_index(head,  i):
    local = 0
    while head.next != None:
        local += 1
        if local == i:
            obj = head.next
            head.next = obj.next
        else:
            head = head.next


arr = [2, 3, 4, 5]
ind = 3

head = linked_list_add(arr, 0)

adding_at_index(head, 100, 2)

link = linked_list(head)
print("Before removing")
link.printing_linked_list()
remove_at_index(head, ind)
print("After removing")
link = linked_list(head)
link.printing_linked_list()
