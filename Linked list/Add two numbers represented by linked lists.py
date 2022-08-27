from linked_list import *


def add_two_linkedlist(first, second):
    num1 = ""
    num2 = ""
    while first or second:
        if first != None:
            num1 = num1+str(first.data)
            first = first.next
        elif second:
            num2 = num2+str(second.data)
            second = second.next
        if first == None and second == None:
            break

    return int(num1) + int(num2)


def reverse_(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def insertAtTail(head, tail, val):
    temp = node(val)
    if head:
        head = temp
        tail = temp
    else:
        tail.next = temp
        tail = temp
    return temp


def add_two_linkedlist_2(first, second):
    first_c = first
    second_c = second
    first_r = reverse_(first_c)
    second_r = reverse_(second_c)

    carry = 0
    head_ans = node(-1)
    ans = head_ans
    while first_r and second_r:
        sumi = first_r.data+carry+second_r.data

        digit = sumi % 10
        new = node(digit)

        ans.next = new
        ans = new

        carry = sumi//10
        first_r = first_r.next
        second_r = second_r.next

    while first_r:
        sumi = first_r.data+carry
        digit = sumi % 10
        new = node(digit)

        ans.next = new
        ans = new
        carry = sumi//10
        first_r = first_r.next
    while second_r:
        sumi = second_r.data+carry
        digit = sumi % 10

        new = node(digit)

        ans.next = new
        ans = new
        carry = sumi//10
        second_r = second_r.next

    while carry:
        digit = carry % 10
        new = node(digit)
        ans.next = new
        ans = new
        carry = carry//10
    return head_ans.next


if __name__ == "__main__":
    arr = [1, 8]
    brr = [4, 5, 2]
    linked_list_1 = linked(None)
    linked_list_1.create_ll(arr)
    head_1 = linked_list_1.head.next
    linked_list_1 = linked(None)
    linked_list_1.create_ll(brr)
    head_2 = linked_list_1.head.next

    answer = add_two_linkedlist_2(head_1, head_2)
    reverse_ans = reverse_(answer)
    linked.printing_linked_list_external(reverse_ans)
