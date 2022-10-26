# Merge k sorted lists
# url  : https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
import queue


class Node:
    def __init__(self, x):

        self.data = x
        self.next = None

    # def __gt__(self, other):
    #     if(self.data > other.data):
    #         return True
    #     else:
    #         return False

    # def __lt__(self, other):
    #     if(self.data < other.data):
    #         return True
    #     else:
    #         return False

    # def __eq__(self, other):
    #     if(self.data == other.data):
    #         return True
    #     else:
    #         return False


class customerNode:
    def __init__(self, x, next=None):

        self.data = x
        self.next = next

    def __gt__(self, other):
        if(self.data > other.data):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.data < other.data):
            return True
        else:
            return False

    def __eq__(self, other):
        if(self.data == other.data):
            return True
        else:
            return False


def mergeKLinkedList(listing):
    minQ = queue.PriorityQueue()
    k = len(listing)
    for linkedList in listing:
        newNode = customerNode(linkedList.data, linkedList.next)
        minQ.put(newNode)

    arr = []
    head = Node(-1)
    curr = head
    while not(minQ.empty()):
        letter = minQ.get()
        newNode = Node(letter.data)
        curr.next = newNode
        curr = newNode
        arr.append(letter.data)
        if letter and letter.next:
            newNode = customerNode(letter.next.data, letter.next.next)
            minQ.put(newNode)

    return(head.next)


if __name__ == '__main__':

    k = 3
    n = 4
    arr = [None for i in range(k)]

    arra = [1, 3, 5, 7, 2, 4, 6, 8, 0, 9, 10, 11]
    print(sorted(arra))
    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)

    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)

    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)
    finalLinkedList = mergeKLinkedList([[]])

    curr = finalLinkedList
    while curr:
        print(curr.data)
        curr = curr.next
