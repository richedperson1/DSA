

arr = [1, 2, 3, 4, 4]
x1 = arr[0]
x2 = 0

for ind, data in enumerate(arr):
    x2 ^= ind
    x1 ^= data
print(x1 ^ x2)
