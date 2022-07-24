arr = [15, 2, 4, 7, -4, -3, -4]
arr = list(map(int, "8 -7 -1 6 -2 1 -3 1 -3".split()))

ans = 0
dist = {}
cumsum = 0
for ind, num in enumerate(arr):
    cumsum += num
    print(cumsum, end="-->")
    if -cumsum in dist:
        local = ind-dist[-cumsum]
        ans = max(local, ans)

    if cumsum in dist:
        local = ind-dist[cumsum]
        ans = max(local, ans)
        # dist[cumsum] = ind
    else:
        dist[cumsum] = ind
print()
print(ans)
