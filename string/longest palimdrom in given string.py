string = "babad"


letter = "aa"

string2 = "aabac"


def palim(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]


def checkingLongPalim(s):
    n = len(s)
    res = ""
    for i in range(n):
        p1 = palim(s, i, i)
        p2 = palim(s, i, i+1)
        if len(p1) > len(res):
            res = p1
        if len(p2) > len(res):
            res = p2

    return res
