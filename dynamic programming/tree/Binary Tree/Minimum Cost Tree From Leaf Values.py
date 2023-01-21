arr = [6, 2, 4]


def miniCost(arr, lft, rgt):
    if lft >= rgt:
        return 0

    final = float("inf")
    for ind in range(lft, rgt):
        ans = max(arr[lft:ind+1])*max(arr[ind+1:rgt+1])

        final = min(final, ans + miniCost(arr, lft, ind) +
                    miniCost(arr, ind+1, rgt))

    return final


def miniCostDP(arr, lft, rgt, dp):
    if lft >= rgt:
        return 0
    if dp[lft][rgt] != -1:
        return dp[lft][rgt]

    final = float("inf")
    for ind in range(lft, rgt):

        ans = max(arr[lft:ind+1])*max(arr[ind+1:rgt+1])

        final = min(final, ans + miniCostDP(arr, ind+1, rgt, dp) +
                    miniCostDP(arr, ind+1, rgt, dp))

    dp[lft][rgt] = final
    return final


print(miniCost(arr, 0, 2))
