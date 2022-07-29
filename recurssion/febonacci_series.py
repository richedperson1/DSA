
# def febo(num):
#     if num <= 1:
#         return num
#     return febo(num-2)+febo(num-1)


# print(febo(num))


def febo_update(n):
    if n <= 1:
        print(n, end="-->")
        return 1
    return febo_update(n-1)+febo_update(n-2)


print(febo_update(5))
