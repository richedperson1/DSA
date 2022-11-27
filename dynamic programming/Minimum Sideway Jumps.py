"""
URL : https://leetcode.com/problems/minimum-sideway-jumps/
"""

import sys
sys.setrecursionlimit(350000000)
"""
Using recurssion approach
"""


def miniJump(arr, curr, ind):
    # if frong jump at last position no need to count it
    # Base condition
    if ind >= len(arr)-1:
        return 0

    ans = sys.maxsize

    if arr[ind+1] == curr:
        for i in range(1, 4):
            if i != curr and arr[ind] != i:
                local = miniJump(arr, i, ind)+1
                ans = min(local, ans)

    else:
        ans = miniJump(arr, curr, ind+1)

    return ans


"""
Using DP approach
"""


def miniJumpDP(arr, curr, ind, dp):
    # if frong jump at last position no need to count it
    # Base condition
    if ind >= len(arr)-1:
        return 0

    ans = sys.maxsize
    if dp[curr][ind] != -1:
        return dp[curr][ind]

    if arr[ind+1] == curr:
        for i in range(1, 4):
            if i != curr and arr[ind] != i:
                local = miniJumpDP(arr, i, ind, dp)+1
                ans = min(local, ans)
    else:
        ans = miniJumpDP(arr, curr, ind+1, dp)

    dp[curr][ind] = ans

    return ans


"""
Tabulation DP : 
Bottom to Top approach
"""


def miniJumpDP_Tab(arr):
    n = len(arr)
    dp = [[sys.maxsize-9]*(n+1) for i in range(4)]

    dp[0][n] = 0
    dp[1][n] = 0
    dp[2][n] = 0
    dp[3][n] = 0

    for i in range(n-1, -1, -1):

        for lane in range(1, 4):
            if arr[i] != lane:
                dp[lane][i] = dp[lane][i+1]
            else:
                ans = sys.maxsize
                for currL in range(1, 4):
                    if currL != lane and arr[i] != currL:
                        local = dp[currL][i+1]+1
                        ans = min(ans, local)

                dp[lane][i] = ans

    return min(dp[1][0]+1, dp[2][0], dp[3][0]+1)


"""
Space optimize solution
"""


def miniDP_space(arr):
    n = len(arr)
    curr = [0, 0, 0, 0]
    next = [0, 0, 0, 0]

    for i in range(n-1, -1, -1):
        for currPos in range(1, 4):
            if arr[i+1] != currPos:
                curr[currPos] = next[currPos]

            else:
                ans = sys.maxsize
                for currLane in range(1, 4):
                    if currLane != currPos and arr[i] != currLane:
                        local = next[currLane]
                        ans = min(local, ans)+1

                curr[currPos] = ans
        next = curr
    return curr


obst = [0, 2, 1, 1, 3, 0]
# obst = [0, 1, 2, 3, 0]
n = len(obst)
dp = [[-1]*(n+1) for i in range(4)]
print(miniJump(obst, 2, 0))
print(miniJumpDP(obst, 2, 0, dp))
print(miniJumpDP_Tab(obst))
print(miniDP_space(obst))
