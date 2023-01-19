arr = [4, 5]
k = 5


def divisibleBy4(arr, k):
    dist = {0: 1}
    currSum = 0
    total = 0
    for ind, data in enumerate(arr):
        currSum += data

        remain = currSum % k
        if remain in dist:
            total += dist[remain]
            dist[remain] += 1
        else:
            dist[currSum] = 1

    return total


print(divisibleBy4(arr, k))
