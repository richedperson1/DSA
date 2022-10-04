import heapq
# heap = heapq
k = 4
items = [2, 5, 7, 80, 30, 12, 59, 63]
heap = []
for item in items:
    if len(heap) < k:
        heapq.heappush(heap, -item)
    else:
        if -1*heap[0] > item:
            # heap = heap[1:]
            heapq.heappop(heap)
            heapq.heappush(heap, -item)
            continue

# print(heap)
heapq.heapify(items)
print(heapq.nsmallest(5, items))
