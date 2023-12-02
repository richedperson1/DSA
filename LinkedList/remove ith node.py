class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return self.data


def remove_ith_node(head, index):
    total = 0
    if index == 1:
        head = head.next
        return head
    # curr = head
    while head:
        total += 1
        if total == index:
            require = head.next
            actual = require.next
            head.next = actual
            break
        else:
            head = head.next

    return head


def create_LL(head, arr):
    while head.next != None:
        head = head.next

    for num in arr:
        new = node(num)
        head.next = new
        head = new

    return head


def print_LL(head):
    while head:
        if head.next == None:
            print(head.data)

        else:
            print(head.data, end=" ----> ")
        head = head.next


if __name__ == "__main__":
    first = node(5)
    arr = [2, 3, 4, 5, 6, 0]
    create_LL(first, arr)
    print_LL(first)
    head = remove_ith_node(first, 4)
    print_LL(first)
