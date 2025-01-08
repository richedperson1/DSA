from functools import total_ordering
import heapq
  
@total_ordering
class Wrapper:
    def __init__(self, val):
        self.val = val
 
    def __lt__(self, other):
        return self.val > other.val
 
    def __eq__(self, other):
        return self.val == other.val
 
 
# heap = [10, 20, 400, 30]
gifts = [25,64,9,4,100] 
k = 4
wrapper_heap = list(map(lambda item: Wrapper(item), gifts))
 
 


heapq.heapify(wrapper_heap)
max_item = heapq.heappop(wrapper_heap)
heapq.heappush(260,wrapper_heap)
# max_item = heapq.heappop(wrapper_heap)
# # This will give the max value
# print(f"Top of numbers are: {max_item.val}")