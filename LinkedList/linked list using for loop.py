class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return self.data


def take_input():
    """
    Adding element into linked list from front

    Time Complexity O(n^2)

    """
    input_list = [2, 3, 5, 6, 9, 8]
    head = None
    for curr in input_list:
        current = node(curr)
        if head is None:
            head = current

        else:
            curr = head
            while curr.next != None:
                curr = curr.next
            curr.next = current
    return head


def take_input_list(head):
    """
    Adding element into linked list from backward

    Time Complexity O(n)

    """
    input_list = [2*i for i in range(1, 10)]
    n = len(input_list)
    i = n-2

    first = node(input_list[-1], None)
    while i >= 0:
        new = node(input_list[i], first)
        first = new
        i -= 1
    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = new
    return head


def adding_ll_with_arr(head):
    arr = [20, 10, 59, 39, 36]
    while head.next:
        head = head.next

    current_head = head
    for num in arr:
        make = node(num)
        current_head.next = make
        current_head = make
    # return head


def printing_linked_list(head):
    """
    This function printing linked list elements

    """
    while head is not None:
        if head.next is None:
            print(head.data, end="")
        else:
            print(head.data, end=' ----> ')
        head = head.next
    print('')
    # print(head.data)


if __name__ == "__main__":
    # start = take_input()
    # printing_linked_list(start)
    # new = take_input_list(start)
    # printing_linked_list(new)

    first = node(5)
    adding_ll_with_arr(first)
    printing_linked_list(first)
