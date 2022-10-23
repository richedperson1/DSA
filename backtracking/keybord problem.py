map = {2: "abc", 3: "def", 4: "ghi"}

ans = []

# Method 1

# def printKeyBordSub(num):
#     if len(num) <= 0:

#         return [""]

#     ans = printKeyBordSub(num[1:])
#     string = map[int(num[0])]
#     rang = len(ans)
#     newAns = []
#     for i in range(rang):
#         for j in range(len(string)):
#             new = ans[i]+string[j]
#             newAns.append(new)

#     return newAns


# ans = printKeyBordSub("23")

# print(ans)
# print(len(ans))


# Method 2
def printKeyBordSub(num):
    if num <= 0:

        return [""]

    smallerNum = num//10
    lastDigit = num % 10

    smallOut = printKeyBordSub(smallerNum)
    string = map[lastDigit]
    newAns = []
    for outS in smallOut:
        for char in string:
            option = outS+char
            newAns.append(option)
    return newAns


ans = printKeyBordSub(23)

print(ans)
print(len(ans))
