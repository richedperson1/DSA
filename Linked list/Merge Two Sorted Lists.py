from heapq import merge
from linked_list import *


def merge_two(first, second):
    if first == None:
        return second
    if second == None:
        return first

    if first.data >= second.data:
        second.next = merge_two(first, second.next)
        return second
    else:
        first.next = merge_two(first.next, second)
        return first


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    brr = [1, 3, 5, 6]
    head_1 = node(arr[0])
    head_2 = node(brr[0])
    first = linked(head_1).create_ll(arr[1:])
    second = linked(head_2).create_ll(brr[1:])
    final = merge_two(first, second)
    linked.printing_linked_list_external(final)
