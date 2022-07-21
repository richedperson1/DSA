arr = [1, 2, 3, 1]


k = 3
cumsum = 0
dist = {0: 1}
ans = 0
for num in arr:
    cumsum += num
    check = cumsum-k
    if check in dist:
        ans += dist[check]
    if cumsum in dist:
        dist[cumsum] += 1

    else:
        dist[cumsum] = 1

print(ans)
