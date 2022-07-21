arr = [1, 1]

total = sum(arr)
n = len(arr)
if n <= 1:
    print(1)
    quit()
prefix = arr[0]
for i in range(1, n):
    local = total-prefix-arr[i]
    if local == prefix:
        print(i+1)
        quit()
    prefix += arr[i]
print(-1)

# 5
# 1 3 5 2 2
