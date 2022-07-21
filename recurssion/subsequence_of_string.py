from operator import sub


arr = 'abc'


def subsequence(arr, local, ans, i):
    if len(arr) == i:
        ans.append(local)
        return
    subsequence(arr, local+[arr[i]], ans, i+1)
    subsequence(arr, local, ans, i+1)
    return ans


ans = []
print(subsequence(arr, [], ans, 0))
print(ans)
