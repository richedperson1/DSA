

arr = [1, 5, 11, 5]


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


print(PartitionSum(0, arr, 0, 0))

sumi = sum(arr)
n = len(arr)

dp = [[[-1]*(n+1) for i in range(sumi+1)] for j in range(sumi+1)]


print(PartitionSumDP(0, arr, 0, 0, dp))
