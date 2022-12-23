"""
URL : https://www.pepcoding.com/resources/online-java-foundation/dynamic-programming-and-greedy/partition-into-subsets-official/ojquestion

"""


"""
Time complexity : O(n^2)
space complexity : O(n)
"""


def divideDP(n, k, dp):
    if n == 0 or k == 0 or n < k:
        return 0

    if k == 1 or k == n:
        return 1

    if dp[n][k] != -1:
        return dp[n][k]

    final = divideDP(n-1, k-1, dp)*k + divideDP(n-1, k, dp)
    dp[n][k] = final
