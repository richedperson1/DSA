

def permutation(string):

    ans = []
    for ind, letter in enumerate(string):
        if string[ind].isnumeric():
            continue
        else:
            new1 = string[:ind]+string[ind].upper()+string[ind+1:]
            new2 = string[:ind]+string[ind].lower()+string[ind+1:]
            ans.append(new1)
            ans.append(new2)

    return ans


print(permutation("a1b2"))
