""""
URL : https://leetcode.com/problems/unique-binary-search-trees/description/
"""

"""
Recursive approach

Time complexity : O(2^n)
Space complexity : O(n) : stack spance only
"""


def ansDP(n, dp):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]
    ans = 0
    for i in range(1, n+1):
        local = ansDP(i-1, dp)*ansDP(n-i, dp)
        ans += local

    dp[n] = ans

    return ans


"""
Tabular approach

Time complexity : O(2^n)
Space complexity : O(n) DP space
"""


def uniqueBST_tab(n):
    dp = [-1]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for j in range(2, n+1):
        ans = 0
        for i in range(1, j+1):
            local = dp[i-1]*dp[j-i]
            ans += local
        dp[j] = ans
    return dp[n]


n = 3
dp = [-1]*(n+1)
print(uniqueBST_tab(n))
