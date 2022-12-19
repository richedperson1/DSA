import math
arr = list(
    map(str, "abbdbdb eacbc edab ebdcdbacdd acdabaa b b e bbccbbabad bedbc".split()))


print(arr)
start = [0]*26

for word in arr:
    print(word)
    letter = word[0]
    ind = 97-ord(letter)

    start[ind] += 1

final = 0
for num in start:

    if num == 1:
        final += 0
    else:
        final += math.ceil(num/2)

print(start)
print(final)
# print(math.ceil(0.5))ṇ
