# Method 1

# def formString(string, n, ans):
#     if len(string) == n:
#         ans.append(string)
#         return ans

#     if string != "" and string[-1] == "0":
#         ans = formString(string+"0", n, ans)
#         ans = formString(string+"1", n, ans)
#     elif string != "" and string[-1] == "1":
#         ans = formString(string+"0", n, ans)

#     elif string == "":
#         ans = formString("0", n, ans)
#         ans = formString("1", n, ans)

#     return ans


# print(formString("", 2, []))


# Method 2

def formString(string, n, ans):
    if len(string) == n:
        ans.append(string)
        return ans

    if string != "":
        if string[-1] == "0":
            ans = formString(string+"1", n, ans)
            ans = formString(string+"0", n, ans)
        else:
            ans = formString(string+"0", n, ans)

    else:
        ans = formString("0", n, ans)
        ans = formString("1", n, ans)

    return ans


print(formString("", 2, []))
