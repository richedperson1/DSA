# import heapq


# def getKthLargest(arr, k):
#     #	Write your code here.
#     totals = []
#     for i in range(len(arr)):
#         total = 0
#         for j in range(i, len(arr)):
#             total += arr[j]
#             if len(totals) == k:
#                 if total > min(totals):
#                     # totals = totals[1:]
#                     totals.remove(min(totals))
#                     totals.append(total)

#             elif len(totals) < 3:
#                 totals.append(total)

#     heapq.heapify(totals)
#     ans = heapq.nlargest(k, totals)

#     return ans


# arr = [5, 4, -8, 6]
# print(getKthLargest(arr, 10))


import heapq

import queue


def getKthLargest(arr, k):
    #	Write your code here.
    totals = []
    sumi_total = queue.PriorityQueue()

    print(sumi_total.qsize())
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            totals.append(total)

    return heapq.nlargest(k, totals)[-1]


arr = [5, 4, -8, 6]
print(getKthLargest(arr, 2))
