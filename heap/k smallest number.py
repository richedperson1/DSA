# import heapq
from heapClass import *
# heap = heapq

##
""" 
Method 1 using heapq class

"""
# k = 4
# items = [2, 5, 7, 80, 30, 12, 59, 63]
# heap = []
# for item in items:
#     if len(heap) < k:
#         heapq.heappush(heap, -item)
#     else:
#         if -1*heap[0] > item:
#             # heap = heap[1:]
#             heapq.heappop(heap)
#             heapq.heappush(heap, -item)
#             continue

# heapq.heapify(items)
# print(heapq.nsmallest(5, items))


""" 
Method 2 using custom class

"""


class ksmallest(heap):
    def ksmall(self, arr, k):
        for num in arr:

            if self.size < k:
                self.insert(num)
            elif self.size >= k and self.storage[1] > num:
                self.delete()
                self.insert(num)
        return self.storage[1:]


arr = [2, 13, 4, 10, 19, 16, 12, 36]
k = 3
print(sorted(arr)[:k][::-1])
ans = ksmallest().ksmall(arr, k)
print(ans)
