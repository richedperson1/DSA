from linked_list import *


class Node(node):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.random = None


def copyList(head):
    # code here
    dist = {None: None}
    curr = head
    while curr:
        copy = Node(curr.data)
        dist[curr] = copy
        curr = curr.next

    curr = head
    while curr:
        temp = dist[curr]
        temp.next = dist[curr.next]
        temp.abs = dist[curr.abs]
    return dist[head]


head = Node(5)
