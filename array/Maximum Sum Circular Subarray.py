def maxiSumSubarray(arr):
    n = len(arr)
    currMax = arr[0]
    globalMax = arr[0]
    for i in range(1, n):
        currMax = max(currMax+arr[i], arr[i])
        globalMax = max(globalMax, currMax)

    leftMax = [0]*n
    currMax = 0
    for i in range(n-1, -1, -1):
        currMax += arr[i]
        leftMax[i] = currMax

    left = leftMax[-1]
    for i in range(n-1, -1, -1):
        left = max(left, leftMax[i])
        leftMax[i] = left

    print(leftMax)
    currMaxRight = 0
    final = float("-inf")
    n = len(leftMax)
    for i in range(n-1):
        currMaxRight += arr[i]
        # print(currMax)
        # currMaxRight +=
        final = max(final, currMaxRight+leftMax[i+1])

    return max(globalMax, final)


arr = [1, -2, 3, -2]
print(maxiSumSubarray(arr))
