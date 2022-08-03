string = 'aazbbby'

# Method 1


def remove_duplicate(string):
    if len(string) <= 1:
        return string

    if string[0] == string[1]:
        total = 0
        for i in range(0, len(string)-1):
            if string[i] == string[i+1]:
                total += 1
            else:
                break
        small = remove_duplicate(string[total+1:])
        return string[0]+small
    else:
        small = remove_duplicate(string[1:])
        return string[0]+small

# method 2


def remove_duplicate_2(string):
    if len(string) < 2:
        return string
    if string[0] != string[1]:
        small = remove_duplicate_2(string[1:])
        return string[0]+small
    else:
        small = remove_duplicate_2(string[1:])
        return small


print(remove_duplicate(string))
print(remove_duplicate_2(string))
