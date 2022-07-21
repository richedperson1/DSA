string = "mam"


def check_palimdrom(string, i, j, flag):
    if i < j:
        flag = string[i] == string[j]
        check_palimdrom(string, i+1, j-1, flag)
        if flag == False:
            return flag
    return flag


print(check_palimdrom(string, 0, len(string)-1, False))
