arr = [16, 17, 4, 3, 5, 2]
n = len(arr)

# brute force approach
ans = []
for i in range(n):
    event = True
    for j in range(i+1, n):
        if arr[i] <= arr[j]:
            event = False
            break
    if event:
        ans.append(arr[i])

# Optimize way

ans1 = []
big = -1
i = n-1
while i >= 0:
    if arr[i] > big:
        ans1.append(arr[i])
        big = arr[i]
    i -= 1
print(ans1[::-1])
