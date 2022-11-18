import sys
num = 12

"""
Brute force
without having minimum choice logic [Dump model]
"""


def minimumNum(num: int) -> int:
    if num <= 0:
        return 0
    if num == 1:
        return 1
    if num == 2:
        return 2

    ans = 0
    local = num - int(num**0.5)**2

    ans = 1 + minimumNum(local)
    return ans


"""
Brute force approach
Using choices and decision

Time complexity : O(n*n^n)
"""


def minimumNumChoice(num: int) -> int:
    if num <= 0:
        return 0
    if num <= 2:
        return num

    ans = sys.maxsize
    for i in range(1, int(num**0.5)+1):
        local = num-i*i
        ans = min(ans, minimumNumChoice(local)+1)
    return ans


"""
DP solution (Tabulation and memosition)
Time complexity : O(n*sqrt(n))
Space complexity : O(n)
"""


def minimumNumChoiceDP(num: int, dp: list[int]) -> int:
    if num <= 0:
        return 0
    if num <= 2:
        return num

    if dp[num] != -4:
        return dp[num]

    ans = sys.maxsize
    maxR = int(num**0.5)+1
    for i in range(1, maxR):
        local = num-i*i
        ans = min(ans, minimumNumChoiceDP(local, dp)+1)
    dp[num] = ans
    return ans


def miniNumDP_Tab(num):
    dp = [num]*(num+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for i in range(3, num+1):
        calling = int(num**0.5)+1
        for j in range(1, calling):
            local = j*j
            if i-local >= 0:
                dp[i] = min(dp[i], dp[i-local]+1)
    return dp[-1]


num = 12
print(miniNumDP_Tab(num))
# for ii in range(5, 50):
#     print("The number is : ", ii)
#     print("Using Dump recursion : ", minimumNum(ii))
#     dp = [-4]*(ii+1)
#     print("Using smart DP : ", minimumNumChoiceDP(ii, dp))
#     print()
