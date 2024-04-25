

def first():
    print("first function", a)

    def second():
        c = 20
        print("Inside second function", a)
    second()


def firsttry():
    try:
        a = 5
        b = 6
        return 256, 785
    finally:
        return 459, 3669


a = 5
aa = "5"
# print(a is aa)


def myfunc1():
    x = "John"

    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x


print(myfunc1())

