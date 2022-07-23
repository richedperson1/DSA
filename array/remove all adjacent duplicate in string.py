string = "geeksforgeek"


def remove(string):
    ans = ""
    i = 0
    while i < len(string):
        if i < len(string)-1 and string[i] == string[i+1]:
            while i < len(string)-1 and string[i] == string[i+1]:
                i += 1
        else:
            ans += string[i]

        i += 1
    return ans


new = ""
while len(string) != len(new):
    new = string
    string = remove(string)

print(string)
