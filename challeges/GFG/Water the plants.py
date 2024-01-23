def min_sprinklers( gallery, n):
    # code here
    intervals = sorted([(i-g, i+g,i) for i, g in enumerate(gallery) if g != -1])
    reachable, best, res = 0, 0, 0
    print(intervals)
    while reachable < n:
        if intervals and intervals[0][0] <= reachable:
            s, e,i = intervals.pop(0)
            best = max(best, e+1)
        elif best > reachable:
            reachable = best
            res += 1
        else:
            return -1
    return res


galary = [-1, 7, 7, 7]
n = len(galary)
print(min_sprinklers(galary,n))