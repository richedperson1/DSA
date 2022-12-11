alphabet = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
            14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}


def totalWay(num, ind):
    if ind >= len(num):
        return 1

    if num[ind] == "0":
        return 0
    res = totalWay(num, ind+1)

    if (ind+1 < len(num)) and (int(num[ind]) == 2 or int(num[ind]) == 1):
        res += totalWay(num, ind+2)

    return res


def totalWayDP(num, ind, dp):
    if ind >= len(num):
        return 1

    if dp[ind] != -1:
        return dp[ind]

    if num[ind] == "0":
        return 0
    res = totalWayDP(num, ind+1, dp)

    if (ind+1 < len(num)) and (int(num[ind]) == 2 or int(num[ind]) == 1):
        res += totalWayDP(num, ind+2, dp)

    dp[ind] = res
    return res


num = "12493"
n = len(num)
dp = [-1]*(n+1)
print(totalWay(num, 0))
print(totalWayDP(num, 0, dp))
