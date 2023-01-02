def checkCap(word):
    first = word.isupper()
    second = word.islower()
    third = word.capitalize() == word
    if first or second or third:
        return True
    else:
        return False


aa = "abcd"
print(aa.isupper())
