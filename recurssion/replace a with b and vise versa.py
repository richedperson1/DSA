string = " s"

# Using another varible to modified string


def modifing_str(string, ans, i, a, b):
    if i == len(string):
        return ans
    if string[i] == a:
        ans += b
    else:
        ans += string[i]

    return modifing_str(string, ans, i+1, a, b)

# Methods 2
# Not using index for string and external varible to store the answer


def modifing_str2(string, a='a', b='b'):
    if len(string) == 0:
        return ""
    small = modifing_str2(string[1:], a, b)

    if string[0] != a:
        return string[0]+small
    else:
        return b+small
    # if small != "":
    #     if string[0] != 'a':
    #         return string[0]+small
    #     else:
    #         return 'b'+small
    # else:
    #     if string[0] != 'a':
    #         return string[0]
    #     else:
    #         return 'b'


string = "cy"
ans0 = modifing_str2(string, 'c', 'y')
ans1 = modifing_str(string, '', 0, 'c', 'y')
print(ans0)
print(ans1)
print(ans0 == ans1)
