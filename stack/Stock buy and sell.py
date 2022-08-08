"""
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Note: Since there can be multiple solutions, the driver code will return 1 if your answer is correct, otherwise, it will return 0. In case there's no profit the driver code will return the string "No Profit" for a correct solution.

Example 1:

Input:
N = 7
A[] = {100,180,260,310,40,535,695}
Output:
1

"""


class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, arr, n):
        stack = []
        for i in range(n-1, -1, -1):
            if not stack:
                stack.append(i)
            if stack and arr[stack[-1]] < arr[i]:
                stack.append(i)

        j = 0
        i = n-1
        while j < n:
            if j < n and arr[j] < arr[stack[-1]]:
                return 1
            else:
                j += 1
        return 0


arr = [100, 180, 260, 310, 40, 535, 695]

obj = Solution().stockBuySell(arr, len(arr))
print(obj)
