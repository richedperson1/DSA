

arr = [1, 5, 11, 14]


def PartitionSum(ind, arr, t1, t2):
    if ind >= len(arr):
        if t1 == t2:
            return 1

        return 0

    final1 = PartitionSum(ind+1, arr, t1+arr[ind], t2)
    final2 = PartitionSum(ind+1, arr, t1, t2+arr[ind])

    return max(final1, final2)


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


def partiesSum(ind, arr, x, sumi):
    if ind >= len(arr):
        return 0

    if x == sumi:
        return 1

    inc = partiesSum(ind+1, arr, x, sumi+arr[ind])
    enc = partiesSum(ind+1, arr, x, sumi)

    return max(inc, enc)


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


print(PartitionSum(0, arr, 0, 0))

sumi = sum(arr)
n = len(arr)

dp = [[[-1]*(n+1) for i in range(sumi+1)] for j in range(sumi+1)]


print(PartitionSumDP(0, arr, 0, 0, dp))

if sumi & 1 == 0:
    tar = sumi//2
    print(partiesSum(0, arr, tar, 0))
    dp = [[-1]*(len(arr)+1) for j in range(tar+1)]
    print(partiesSumDP(0, arr, tar, 0, dp))
