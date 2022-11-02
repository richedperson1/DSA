arr = [10, 25, 50, 70, 90, 100]
n = len(arr)
# Method 1

"""
It using recursion to find the solution 
which Time complexity : O(2^n)

space complexity : O(n^2)
"""


def select_match(arr, local, ans, ind, cnt):
    if ind >= len(arr):
        if ans == []:
            ans.append(sum(local))
        else:
            ans[-1] = max(ans[-1], sum(local))
        return

    if cnt >= 2:
        select_match(arr, local, ans, ind+1, 0)
    else:

        select_match(arr, local+[arr[ind]], ans, ind+1, cnt+1)
        select_match(arr, local, ans, ind+1, 0)


ans = []
# select_match(arr, [], ans, 0, 0)
# print(ans)


# Method 2

"""
By using dp problem
"""

dp = [0]*n
dp[0] = arr[0]
dp[1] = arr[1]
dp[2] = arr[2]

for i in range(3, n):
    mini = min(dp[i-1], dp[i-2], dp[i-3])+arr[i]
    dp[i] = mini

final = sum(arr)-min(dp[-3:])

print(final)
