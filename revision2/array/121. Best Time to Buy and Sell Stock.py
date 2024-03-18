
arr = [7,1,5,3,6,4]

def bestTimeStockSell():
    profit = 0

    size = len(arr)
    for ind in range(size):
        localProfit = 0
        for ind2 in range(ind,size):
            localProfit = max(localProfit,arr[ind2]-arr[ind])

        profit = max(profit,localProfit)

    return profit


def bestTimeStockSellBeter():
    size = len(arr)
    stack = [0]*size

    ans = arr[-1]
    profit = 0
    for ind in reversed(range(size)):
        ans = max(ans,arr[ind])
        stack[ind] = ans

    for ind in range(size):
        profit = max(profit,stack[ind]-arr[ind])



    return profit
        

def bestTimeStockSellOptimize():
    size = len(arr)
    profit = 0
    mini = arr[0]
    for ind in range(size):
        mini = min(arr[ind],mini)
        profit = max(arr[ind]-mini,profit)

    return profit


arr = [7,6,5,4,3,2,1]
print(bestTimeStockSell())
print(bestTimeStockSellBeter())
print(bestTimeStockSellOptimize())