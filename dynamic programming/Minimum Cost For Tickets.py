"""
URL : https://leetcode.com/problems/minimum-cost-for-tickets/

"""


"""
Discription :

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.


Example 1:

    Input: days = [1,4,6,7,8,20], costs = [2,7,15]
    Output: 11
    Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
    On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
    On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
    On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
    In total, you spent $11 and covered all the days of your travel.


"""
# We need to call it


"""
Brute force approach
"""




import sys
def miniCostTicket(days, cost, ind, maxR):
    if ind >= len(days):
        return 0

    if days[ind] < maxR:
        return miniCostTicket(days, cost, ind+1, maxR)

    ans = sys.maxsize
    for index, data in enumerate(cost):
        if index == 0:
            maxR = days[ind]+1
            ans = min(ans, miniCostTicket(days, cost, ind+1, maxR)+data)
        elif index == 1:
            maxR = days[ind]+7
            ans = min(ans, miniCostTicket(days, cost, ind+1, maxR)+data)
        else:
            maxR = days[ind]+30
            ans = min(ans, miniCostTicket(days, cost, ind+1, maxR)+data)
    return ans


"""
Using DP approach
"""


def miniCostTicketDP(days, cost, ind, maxR, dp):
    if ind >= len(days):
        return 0

    if days[ind] < maxR:
        return miniCostTicketDP(days, cost, ind+1, maxR, dp)

    if dp[ind] != -4:
        return dp[ind]
    ans = sys.maxsize
    for index, data in enumerate(cost):
        if index == 0:
            maxR = days[ind]+1
            ans = min(ans, miniCostTicketDP(days, cost, ind+1, maxR, dp)+data)
        elif index == 1:
            maxR = days[ind]+7
            ans = min(ans, miniCostTicketDP(days, cost, ind+1, maxR, dp)+data)
        else:
            maxR = days[ind]+30
            ans = min(ans, miniCostTicketDP(days, cost, ind+1, maxR, dp)+data)

    dp[ind] = ans
    return ans


def miniCostTicketDP_2(days, cost, ind, n):
    if ind >= n:
        return 0

    option1 = cost[0]+miniCostTicketDP_2(days, cost, ind+1, n)

    # 15 day trial periods
    ii = ind
    while ii < n and days[ind]+7 > days[ii]:
        ii += 1
    option2 = cost[1]+miniCostTicketDP_2(days, cost, ii, n)

    # 30 day trial periods
    ii = ind
    while ii < n and days[ind]+30 > days[ii]:
        ii += 1
    option3 = cost[2]+miniCostTicketDP_2(days, cost, ii, n)

    return min(option1, option2, option3)


def miniCostDP_Tab(days, cost):
    n = len(days)
    dp = [cost[0]*n]*(n+1)
    dp[-1] = 0

    for kk in range(n-1, -1, -1):
        # For 1 day call
        option1 = dp[kk+1]+cost[0]

        # For 7 day call
        i = kk
        while i < n and days[kk]+7 > days[i]:
            i += 1

        option2 = cost[1]+dp[i]

        # 30 day call
        i = kk
        while i < n and days[kk]+30 > days[i]:
            i += 1

        option3 = cost[2]+dp[i]

        dp[kk] = min(option1, option2, option3)

    return dp[0]


# days = [1, 4, 6, 7, 8, 18]
# costs = [2, 7, 15]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
n = len(days)
dp = [-4]*(n+1)
print(miniCostTicketDP(days, costs, 0, 1, dp))
print(miniCostTicketDP_2(days, costs, 0, len(days)))
print(miniCostDP_Tab(days, costs))
