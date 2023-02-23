import heapq
cap = [0, 1, 1, 2, 3]
profit = [1, 2, 0, 4, 10]

minCap = [(c, p) for c, p in zip(cap, profit)]
print(sorted(minCap))


def maxCapital(capital, profits, w, k):
    minCap = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(minCap)
    maxProfit = []

    for ind in range(k):
        while minCap and minCap[0][0] <= w:
            c, p = heapq.heappop(minCap)
            heapq.heappush(maxProfit, -p)

        if not maxProfit:
            return w
        w += -heapq.heappop(maxProfit)

    return w


def maxCap(capital, profits, w, k):
    minCap = [(c, p) for c, p in zip(capital, profits)]
    minCap = sorted(minCap)
    num = len(minCap)
    prevC = minCap[0][0]
    prevP = minCap[0][1]
    if prevC > w:
        return w
    w += prevP
    rK = 1
    for ind in range(1, num):
        currP = minCap[ind][1]
        currC = minCap[ind][0]
        if prevC == currC:
            if currP > prevP:
                w -= prevP
                w += currP
            # prevC = currC
            # prevP = currP

        else:
            if w < currC:
                break
            elif rK <= k:
                rK += 1
                w += currP
        prevC = currC
        prevP = currP

    return w


print(maxCap(cap, profit, 0, 3))
