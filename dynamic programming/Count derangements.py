"""
A Derangement is a permutation of ‘ N ’ elements, such that no element appears in its original position. 
For example, an instance  of derangement of {0, 1, 2, 3} is {2, 3, 1, 0}, because 2 present at index 0 
is not at its initial position which is 2 and similarly for other elements of the sequence.


URL : https://www.codingninjas.com/codestudio/problems/count-derangements_873861

"""

count = 0


def checking(n):
    global count
    count += 1
    if n <= 0:
        return 1

    return (n-1)*(checking(n-2)+checking(n-1))


countDp = 0


def checking_dp(n, dp):
    global countDp
    countDp += 1
    if n <= 0:
        return 1

    if dp[n] != -1:
        return dp[n]

    maxi = (n-1)*(checking_dp(n-2, dp)+checking_dp(n-1, dp))

    dp[n] = maxi
    return maxi


n = 2999
dp = [-1]*(n+1)
print(checking(n), count)
print(checking_dp(n, dp), countDp)
