arr = [2, 1, 3, 5, 9, 7]


# def merge_final(left, right, arr):
#     l = 0
#     r = 0
#     i = 0
#     while l < len(left) and r < len(right):
#         if left[l] < right(r):
#             arr[i] = left[l]
#             l += 1
#             i += 1
#         else:
#             arr[i] = right[r]
#             r += 1
#             i += 1

#     while l < len(left):
#         arr[i] = left[l]
#         l += 1
#         i += 1
#     while r < len(right):
#         arr[i] = right[r]
#         r += 1
#         i += 1


def divide(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    right = arr[mid:]
    left = arr[0:mid]
    # print(left)
    divide(right)
    divide(left)
    # merge_final(left, right, arr)
    l = 0
    r = 0
    i = 0
    while l < len(left) and r < len(right):
        if left[l] >= right[r]:
            arr[i] = right[r]
            i += 1
            r += 1
        else:
            arr[i] = left[l]
            i += 1
            l += 1
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        arr[i] = right[r]
        i += 1
        r += 1
    # return arr


divide(arr)
print(arr)
