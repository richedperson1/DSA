

arr = [1, 5, 11, 5]
"""
Recursive approach

Time complexity : O(2^n)
space complexity : O(n)
"""


def PartitionSum(ind, arr, t1, t2):
    if ind >= len(arr):
        if t1 == t2:
            return 1

        return 0

    final1 = PartitionSum(ind+1, arr, t1+arr[ind], t2)
    final2 = PartitionSum(ind+1, arr, t1, t2+arr[ind])

    return max(final1, final2)


"""
dp approach

Time complexity : O(n^2)
space complexity : O(n^2)

"""


def PartitionSumDP(ind, arr, t1, t2, dp):
    if ind >= len(arr):
        if t1 == t2:
            return 1

        return 0

    if dp[t1][t2][ind] != -1:
        return dp[t1][t2][ind]

    final1 = PartitionSumDP(ind+1, arr, t1+arr[ind], t2, dp)
    final2 = PartitionSumDP(ind+1, arr, t1, t2+arr[ind], dp)

    ans = max(final1, final2)
    dp[t1][t2][ind] = ans
    return ans


"""
Method 2
Recursive approach

Time complexity : O(2^n)
space complexity : O(n)
"""


def partiesSum(ind, arr, x, sumi):
    if ind >= len(arr):
        return 0

    if x == sumi:
        return 1

    inc = partiesSum(ind+1, arr, x, sumi+arr[ind])
    enc = partiesSum(ind+1, arr, x, sumi)

    return max(inc, enc)


"""
Method 2
dp approach

Time complexity : O(n^2)
space complexity : O(n^2)

"""


def partiesSumDP(ind, arr, x, sumi, dp):
    if ind >= len(arr):
        return 0

    if x == sumi:
        return 1

    if sumi > x:
        return 0

    if dp[sumi][ind] != -1:
        return dp[sumi][ind]

    inc = partiesSumDP(ind+1, arr, x, sumi+arr[ind], dp)
    enc = partiesSumDP(ind+1, arr, x, sumi, dp)
    ans = max(inc, enc)
    dp[sumi][ind] = ans
    return ans


"""
Method 3
dp approach

Time complexity : O(n^2)
space complexity : O(n^2)

"""


def partiesSumDP2(ind, arr, x, dp):
    if ind >= len(arr) or x < 0:
        return 0

    if x == 0:
        return 1

    if dp[x][ind] != -1:
        return dp[sumi][ind]

    inc = partiesSumDP2(ind+1, arr, x-arr[ind], dp)
    enc = partiesSumDP2(ind+1, arr, x, dp)
    ans = max(inc, enc)
    dp[x][ind] = ans
    return ans


"""
Method 3
dp tab approach

Time complexity : O(n^2)
space complexity : O(n^2)

"""


def partiesSumTabDP(arr):
    n = len(arr)
    sumi = sum(arr)
    tar = sumi//2
    if sumi & 1:
        return 0

    dp = [[0]*(len(arr)+2) for j in range(tar+2)]
    for i in range(n):
        dp[0][i] = 1

    for ind in range(n-1, -1, -1):
        for sumi in range(1, tar+1):
            inc = 0
            if sumi-arr[ind] >= 0:
                inc = dp[sumi-arr[ind]][ind+1]
            enc = dp[sumi][ind+1]
            dp[sumi][ind] = max(inc, enc)

    return dp[tar][0]


def partiesSumTabDP_opt(arr):
    n = len(arr)
    sumi = sum(arr)
    tar = sumi//2
    if sumi & 1:
        return 0

    dpNext = [0]*(tar+2)
    dpCurr = [0]*(tar+2)
    dpNext[0] = 1

    for ind in range(n-1, -1, -1):
        for sumi in range(1, tar+1):
            inc = 0
            if sumi-arr[ind] >= 0:
                inc = dpNext[sumi-arr[ind]]
            enc = dpNext[sumi]
            dpCurr[sumi] = max(inc, enc)

        dpNext = dpCurr.copy()

    return dpNext[tar]


print(PartitionSum(0, arr, 0, 0))

arr = [1, 5, 11, 5]
sumi = sum(arr)
n = len(arr)
print("------------>", partiesSumTabDP(arr))
print("------------>", partiesSumTabDP_opt(arr))


# dp = [[[-1]*(n+1) for i in range(sumi+1)] for j in range(sumi+1)]


# if sumi & 1 == 0:
#     tar = sumi//2
#     print(partiesSum(0, arr, tar, 0))
#     dp = [[-1]*(len(arr)+1) for j in range(tar+1)]
#     print(partiesSumDP(0, arr, tar, 0, dp))
#     dp = [[-1]*(len(arr)+1) for j in range(tar+1)]
#     print(partiesSumDP2(0, arr, tar, dp))
