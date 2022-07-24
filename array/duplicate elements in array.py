class Solution:
    def duplicates_1(self, arr, n):
        dist = {}
        for num in arr:
            if num in dist:
                dist[num] += 1
            else:
                dist[num] = 1

        ans = []
        for key, val in dist.items():
            if val > 1:
                ans.append(key)

        return sorted(ans) if len(ans) > 0 else [-1]


def duplicates_2(arr, n):
    arr = sorted(arr)
    ans = []
    i = 0
    while i < n:
        if i < n-1 and arr[i] == arr[i+1]:
            ans.append(arr[i])
            while i < n-1 and arr[i] == arr[i+1]:
                i += 1

        else:
            i += 1
            # continue

    return ans


que_arr = [0, 0]
n = len(que_arr)
print(duplicates_2(que_arr, n))
