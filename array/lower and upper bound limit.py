def numSubarrayBoundedMax(nums: list[int], left: int, right: int):
    curr = 0
    low = 0
    ans = 0
    n = len(nums)
    arr = nums
    for ind in range(n):
        if left >= arr[ind] <= right:
            ans += 1
            if low <= ind:
                continue
            else:
                ans += (low-ind)

        else:
            ans += max(0, (low-ind-1))
    return ans


arr = [2, 1, 4, 3]

print(numSubarrayBoundedMax(arr, 2, 3))
