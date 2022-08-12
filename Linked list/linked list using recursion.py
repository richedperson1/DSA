from os import link


class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def linked_list(arr, i):
    if i == (len(arr)-1):
        return node(arr[i], None)

    node_of_link = linked_list(arr, i+1)
    head = node(arr[i], node_of_link)
    return head


def printing(head):
    if head.next is None:
        print("Linked list is empty")
        return "Linked list is empty"

    iterator = head
    while iterator.next:
        print(iterator.data, " --->", end=' ')
        iterator = iterator.next
    print(iterator.data)


arr = [2, 3, 4, 5, 6]
whole_list = linked_list(arr, 0)
print(whole_list.data)
printing(whole_list)
