arr = arr = list(
    map(int, "87 56 43 91 27 65 59 36 32 51 37 28 75 7 74".split()))


def binarySearch(low, high, want, arr, num):
    while low <= high:
        mid = (low+high)//2
        if arr[mid]+num == want:
            return True

        elif (arr[mid]+num) > want:
            high = mid-1
        else:
            low = mid+1

    return False


def party(arr):
    n = len(arr)
    totalSumi = sum(arr)
    if totalSumi & 1:
        return False

    tarSum = totalSumi//2
    dp = [0]*(n+1)
    lastOne = 0
    local = 0
    ans = False
    for ind, data in enumerate(arr):
        local += data
        if local <= tarSum:
            lastOne = ind
            dp[ind] = local
            if local == tarSum:
                return True

        else:
            ans = binarySearch(0, lastOne, tarSum, dp, data)
            if ans == True:
                return True
    return False


arr = sorted(arr)
print(party(arr))


binary = [1, 2, 3, 4, 5, 6]
print(binarySearch(0, len(binary)-1, 1, binary, 0))
