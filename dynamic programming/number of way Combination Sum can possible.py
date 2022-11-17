"""
Title : Ways to sum to N using array elements with repetition allowed


Given a set of m distinct positive integers and a value ‘N’. The problem is to count the total number of ways we can form ‘N’ by doing sum of the array elements. Repetitions and different arrangements are allowed.

Examples : 

Input: arr = {1, 5, 6}, N = 7
Output: 6
Explanation: The different ways are:
1+1+1+1+1+1+1
1+1+5
1+5+1
5+1+1
1+6
6+1

Input: arr = {12, 3, 1, 9}, N = 14
Output: 150

"""

"""
Brute force approach 

Time complexity : O(n*n^n)
space complexity : O(n)
"""

countSimple = 0


def wayPresent(arr, total, tar):
    global countSimple
    countSimple += 1
    if total == tar:
        return 1

    if total > tar:
        return 0

    ans = 0
    for i, data in enumerate(arr):
        if total+data <= tar:
            ans += wayPresent(arr, total+data, tar)
    return ans


countDP = 0


def wayPresentUsingDP(arr, total, tar, dp):
    global countDP
    countDP += 1
    if total == tar:
        return 1

    if total > tar:
        return 0

    if dp[total] != -4:
        return dp[total]
    ans = 0
    for i, data in enumerate(arr):
        if total+data <= tar:
            ans += wayPresentUsingDP(arr, total+data, tar, dp)
    dp[total] = ans
    return ans


"""
Time complexity : O(n^2)
Space complexity : O(n)

Without using total varible
"""


def solveDP(arr, tar, dp):
    if tar < 0:
        return 0
    if tar == 0:
        return 1
    if dp[tar] != -4:
        return dp[tar]
    ans = 0
    for data in arr:
        if tar-data >= 0:
            ans += solveDP(arr, tar-data, dp)

    dp[tar] = ans
    return ans


"""
Tabular form of DP

"""


def mini_step_tab(arr, tar):
    dp = [0]*(tar+1)
    dp[0] = 1
    for i in range(1, tar+1):
        for j in range(len(arr)):
            if i-arr[j] >= 0:
                dp[i] += dp[i-arr[j]]

    return dp[-1]


arr = [1, 5, 7, 6, 5, 2, 3, 69, 86]
tar = 7
dp = [-4]*(tar+1)

print("Answer using recursion is :", wayPresent(arr, 0, tar))

print("Answer using dp is :", wayPresentUsingDP(arr, 0, tar, dp))
print("Answer using tabular form :", mini_step_tab(arr, tar))
# print("and DP counts is : ", countDP)
