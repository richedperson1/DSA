arr = [2, 3, 1, 6, 8, 4]


def sum_equal_to_k(arr, local, ans, sum, k, i):
    if sum >= k:
        if sum == k:
            ans.append(local)
        return
        ans.append()

    if i >= len(arr):
        if sum == k:
            ans.append(local)
        return
    sum_equal_to_k(arr, local+[arr[i]], ans, int(sum+arr[i]), k, i+1)
    sum_equal_to_k(arr, local, ans, sum, k, i+1)


ans = []
locals = []
k = 12
sum = 0
i = 0
sum_equal_to_k(arr, locals, ans, sum, k, i)
print(sum+arr[i])
print(locals+[arr[i]])

print(ans)
