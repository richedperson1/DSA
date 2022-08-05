arr = [1, 2, 3]

ans = []
k = 4

# when element in subsequence require greater than k


def subsequence(arr, local, ans, i):
    if i == len(arr):
        ans.append(local)
        return

    if local and local[-1] <= k:
        return
    subsequence(arr, local+[arr[i]], ans, i+1)
    if i == 2 and local == []:
        return
    subsequence(arr, local, ans, i+1)
    return ans

# Subsequence from the arrays


def subsequence_2(arr, local, ans1, i):
    if i == len(arr):
        ans1.append(local)
        return
    subsequence_2(arr, local+[arr[i]], ans1, i+1)
    subsequence_2(arr, local, ans1, i+1)
    return ans1


a = subsequence(arr, [], ans, 0)
# print(len(a))
print(a)

# ans1 = []
# a1 = subsequence_2(arr, [], ans1, 0)
# print(len(a1))
# print(a1)
