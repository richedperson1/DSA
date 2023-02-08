
"""
URL : https://leetcode.com/problems/jump-game-ii/description/
"""
import sys


def jump(arr, ind):
    n = len(arr)-1
    if ind >= n:
        return 0

    localJump = arr[ind]
    if localJump == 0:
        return sys.maxsize

    ans = sys.maxsize
    for jum in range(ind+1, ind+localJump+1):
        local = jump(arr, jum)+1
        ans = min(ans, local)

    return ans


def jumpDP(arr, ind, dp):
    n = len(arr)-1
    if ind >= n:
        return 0

    if dp[ind] != -1:
        return dp[ind]

    localJump = arr[ind]
    if localJump == 0:
        return sys.maxsize

    ans = sys.maxsize
    for jum in range(ind+1, ind+localJump+1):
        local = jumpDP(arr, jum, dp)+1
        ans = min(ans, local)

    dp[ind] = ans
    return ans


def jumpOpt(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    last = next = 0
    jump = 1
    for i in range(len(nums)):
        temp = next
        # print(last)
        next = max((nums[j]+j for j in range(last, next+1)))
        if next >= len(nums)-1:
            break
        jump += 1
        last = temp

    return jump


def jumpO(arr):

    next = 0
    last = 0
    step = arr[next]
    n = len(arr)-1
    if n <= 0:
        return 0
    jump = 1
    while next <= n:
        temp = next
        next = max([arr[i]+i for i in range(last, next+1)])
        n = len(arr)-1
        if next >= n:
            break

        last = temp
        jump += 1
    return jump


arr = [1, 2, 3]
num = len(arr)
dp = [-1]*num
print(jump(arr, 0))
print(jumpOpt(arr))
print(jumpO(arr))
print(jumpDP(arr, 0, dp))
