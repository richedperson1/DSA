"""
URL : https://leetcode.com/problems/longest-turbulent-subarray/
"""


def turbulentArr(arr):
    r, l = 1, 0
    ans, prev = 0, ""
    while r < len(arr):
        if arr[r] < arr[r-1] and prev != "<":
            ans = max(ans, r-l+1)
            r += 1
            prev = "<"
        elif arr[r] > arr[r-1] and prev != ">":
            ans = max(ans, r-l+1)
            r += 1
            prev = ">"
        else:
            r = r+1 if arr[r] == arr[r-1] else r
            l = r-1
            prev = ""
    return ans


arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
arr = [4, 8, 12, 16]

print(turbulentArr(arr))
