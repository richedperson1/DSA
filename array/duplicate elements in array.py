# methods 1
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

# methods 2


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
    return ans


# methods 3

que_arr = [1, 3, 4, 2, 2]
n = len(que_arr)
arr = que_arr
slow = 0
fast = 0
while True:
    fast = arr[arr[fast]]
    slow = arr[slow]
    if slow == fast:
        break

find = 0
while find != fast:
    fast = arr[fast]
    find = arr[find]

print(find)
