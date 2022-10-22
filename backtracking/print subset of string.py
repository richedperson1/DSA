string = "abc"

# Method 1
# def subset(string, i, local, ans):
#     if i >= len(string):
#         if local != "":
#             ans.append(local)
#         return

#     subset(string, i+1, local+string[i], ans)
#     subset(string, i+1, local, ans)


# ans = []
# subset(string, 0, "", ans)
# print(ans)


# method 2
ans = []

string = "abc"


def subsetString(string, ans):
    if string == "":
        ans.append(string)
        return ans
    ans = subsetString(string[1:], ans)
    num = len(ans)
    for val in range(num):
        new = string[0]+ans[val]
        ans.append(new)
    return ans


print(subsetString("abcd", ans))
print((ans))
