# Methods 1
arr = [1, 2, 3, 4, 5, 10]
brr = [2, 3, 1, 0, 5]

ans = []
for num in arr:
    if num not in brr:
        ans.append(num)

print(ans)

# Methods 2 This method is work when order of the elements is not matters


def findMissing(arr, brr, n=len(arr), m=len(brr)):
    arr = sorted(arr)
    brr = sorted(brr)
    i = 0
    j = 0
    ans = []
    while i < n and j < m:
        while j < m and brr[j] < arr[i]:
            j += 1
        while i < n and arr[i] < brr[j]:
            ans.append(arr[i])
            i += 1
        if arr[i] == brr[j]:
            i += 1
            j += 1
        else:
            ans.append(arr[i])
            i += 1
            j += 1
    while i < n:
        ans.append(arr[i])
        i += 1
    return ans


print(findMissing(arr, brr,))

# Methods  This method is work at every step
dist = {}
ans = []
for num in brr:
    dist[num] = 1
for num1 in arr:
    if num1 not in dist:
        ans.append(num1)

print(ans)
