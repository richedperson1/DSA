string = "ccabbdaababdacdef"


def checking_string(string):
    patten = "bda"
    total = 0
    for ind, pat in enumerate(patten):
        local = (ord(pat)-ord('a')+1)*(10**(len(patten)-ind))
        total += local

    check = 0
    start = 0
    total_count = 0
    for i in range(len(string)):
        if i < len(patten):
            local = (ord(string[i])-ord('a')+1)*(10**(len(patten)-i))
            check += local

        elif check == total and string[start:i] == patten:
            total_count += 1
            start = i
            # return [start, i]
        else:
            pat = string[i]
            local = (ord(string[start])-ord('a')+1)*(10**len(patten))
            check -= local
            check *= 10
            start += 1
            check += (ord(string[i])-ord('a')+1)*10
            if check == total and string[start:i] == patten:
                total_count += 1
                start = i
    return total_count


print(checking_string(string))
