class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def removeLoop(head: Node) -> Node:

    # Write your code
    curr = head
    if head == None or head.next == None:
        return head
    dist = {}
    dist[head] = head.val
    if True:
        while head:
            if head.next == None:
                return curr
            if head.next in dist:
                head.next = None
                return curr
            head = head.next
            dist[head] = head.val
    return curr
