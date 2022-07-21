# ----------------------------------------| Reverse array | ------------------------------------------------#
arr = [i for i in range(10)]


def printing_reverse(arr):
    if len(arr) == 1:
        return
    ele = arr.pop(0)
    printing_reverse(arr)
    arr.append(ele)


# printing_reverse(arr)
# print((arr))


# ----------------------------------------| Reverse stack |------------------------------------------------ #

arr = [1, 2, 3, 4, 5]


def reverse(arr, ele):
    if len(arr) == 0:
        arr.append(ele)
        return
    alpha = arr.pop()
    reverse(arr, ele)
    arr.append(alpha)


def printing_reverse(arr):
    if len(arr) == 0:
        return
    ele = arr.pop()
    printing_reverse(arr)
    reverse(arr, ele)


printing_reverse(arr)
print((arr))
