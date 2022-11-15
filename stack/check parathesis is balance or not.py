def ispar(x):
    # code here
    arr = [x[0]]
    x = x[1:]
    for ind, data in enumerate(x):

        if data == "[" or data == "(" or data == "{":
            arr.append(data)
        else:
            if data == "}" and len(arr) > 0 and arr[-1] == "{":
                arr.pop()

            elif data == ")" and len(arr) > 0 and arr[-1] == "(":
                arr.pop()

            elif data == "]" and len(arr) > 0 and arr[-1] == "[":
                arr.pop()
            else:
                return False

    if len(arr) == 0:
        return True

    return False


chec = "({[]})"
print(ispar(chec))
