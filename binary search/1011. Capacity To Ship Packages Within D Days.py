"""
URL : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""


def check(arr, k, mini):
    n = len(arr)
    total = 0
    require = 1
    days = k
    for ind in range(n):
        if total+arr[ind] <= mini:
            total += arr[ind]
        else:
            total = arr[ind]
            require += 1
            days -= 1
    if days >= 1:
        return True
    return False


def calCapcity(arr, days):
    low = max(arr)
    high = sum(arr)
    ans = high
    while low <= high:
        mid = (low+high)//2
        if check(arr, days, mid):
            ans = min(mid, ans)
            high = mid-1
        else:
            low = mid+1
    return ans


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(calCapcity(arr, days))
