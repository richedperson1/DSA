test = 5
arr = [2, 8, 6, 16, 5]

dist = {}
m = 10e9+7
maxi = max(arr)
total = 1
for i in range(1, maxi+1):
    total = (total * i) % m
    dist[i] = int(total)
print(dist)
