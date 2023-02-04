

def zigzagCon(string, row):
    form = ""
    n = len(string)
    localPlus = (row-1)*2
    for ind in range(row):
        i = ind
        form += string[i]
        while i < n:
            if i % (row-1) != 0:
                first = i+(row-1-i % (row-1))*2
                if first < n:
                    form += string[first]
                i += localPlus
                if i < n:
                    form += string[i]
            else:
                newI = (row-1)*2
                i = newI+i
                if i < n:
                    form += string[i]

    return form


string = "PAYPALISHIRING"
n = 4
print(zigzagCon(string, n))
