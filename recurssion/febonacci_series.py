num = 4


def febo(num):
    if num <= 1:
        return num
    return febo(num-2)+febo(num-1)


print(febo(num))
