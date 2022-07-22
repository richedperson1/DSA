
arr = [1, 1, 1, 1, 1, 1]
k = 3
n = len(arr)
dist = {0: 1}
cumsum = 0
ans = 0
for ind in arr:
    cumsum += ind

    require = cumsum-k
    if require in dist:
        ans += dist[require]

    if cumsum in dist:
        dist[cumsum] += 1
    else:
        dist[cumsum] = 1
print(ans)
