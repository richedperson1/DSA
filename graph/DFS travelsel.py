from typing import *
from collections import *


def adjecent(ans, u, v):
    ans[u].append(v)
    ans[v].append(u)


def findAdj(edges, dist):
    n = len(edges[0])
    for ind in range(n):
        u = edges[0][ind]
        v = edges[1][ind]
        dist = adjecent(dist, u, v)

    return dist


final = defaultdict(list)
final["u"].append(5)
final["u"].append(50)
print(final)
