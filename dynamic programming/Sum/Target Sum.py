"""
https://leetcode.com/problems/target-sum/

"""


def targetSUM(ind, sumi, tar):
    n = len(arr)
    if ind >= n:
        if sumi == tar:
            return 1
        return 0

    add = targetSUM(ind+1, sumi+arr[ind], tar)
    sub = targetSUM(ind+1, sumi-arr[ind], tar)

    return add+sub


def targetSumDP(arr, ind, dp, tar, sumi):
    n = len(arr)
    if ind >= n:
        if sumi == tar:
            return 1
        return 0

    if (sumi, ind) in dp:
        return dp[(sumi, ind)]

    add = targetSumDP(arr, ind+1, dp, tar, sumi+arr[ind])
    sub = targetSumDP(arr, ind+1, dp, tar, sumi-arr[ind])

    ans = add+sub
    dp[(sumi, ind)] = ans
    return ans


arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
tar = 2
n = len(arr)+1
sumi = sum(arr)
print(targetSUM(0, 0, tar))
print(targetSumDP(arr, 0, {}, tar, 0))
