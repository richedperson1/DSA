from queue import PriorityQueue
q = PriorityQueue()

arr = [20, 17, 5, 369, 36, 14]
for num in arr:
    q.put(num)

# print(q.get())

while not q.empty():
    print(q.get())
