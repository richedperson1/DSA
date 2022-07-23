string = "abccbccba"

i = 0
new = string
while i < len(string):
    j = 0
    form = ""
    if j < len(new)-1 and new[j] == new[j+1]:
        while j < len(new)-1 and new[j] == new[j+1]:
            j += 1
    else:
        new += string[j]

    form = new
    i += 1

print(form)
