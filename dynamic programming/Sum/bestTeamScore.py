

def bestTeam(scores, age, ind, prevI):
    n = len(scores)
    if ind >= n:
        return 0

    inc = 0
    exc = 0
    inc1 = 0
    if(age[prevI] >= age[ind] and scores[prevI] >= scores[ind]) or (age[prevI] <= age[ind] and scores[prevI] <= scores[ind]):
        inc = bestTeam(scores, age, ind+1, ind)+scores[ind]
        inc1 = bestTeam(scores, age, ind+1, prevI)

    else:
        exc = bestTeam(scores, age, ind+1, prevI)

    return max(inc, exc, inc1)


def bestTeamDP(scores, age, ind, prevI, dp):
    n = len(scores)
    if ind >= n:
        return 0

    if dp[ind][prevI] != -1:
        return dp[ind][prevI]

    inc = 0
    exc = 0
    inc1 = 0
    if(age[prevI] >= age[ind] and scores[prevI] >= scores[ind]) or (age[prevI] <= age[ind] and scores[prevI] <= scores[ind]):
        inc = bestTeamDP(scores, age, ind+1, ind, dp)+scores[ind]
        inc1 = bestTeamDP(scores, age, ind+1, prevI, dp)

    else:
        exc = bestTeamDP(scores, age, ind+1, prevI, dp)

    ans = max(inc, exc, inc1)
    dp[ind][prevI] = ans
    return ans


scores = [0] + [4, 5, 6, 5]
ages = [0] + [2, 1, 2, 1]
n = len(ages)+1
dp = [[-1]*n for i in range(n)]
print(bestTeam(scores, ages, 1, 0))
print(bestTeamDP(scores, ages, 1, 0, dp))
