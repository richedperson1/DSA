
from collections import *


def checkAna(s, p):
    numS = len(s)
    numP = len(p)
    if numS < numP:
        return []

    ans = []
    anaDist = Counter(p)
    for ind in range(numS):
        subStr = s[ind:ind+numP]
        subDict = Counter(subStr)
        if subDict == anaDist:
            ans.append(ind)

    return ans


s = "abab"
p = "ab"
s = "abaa"
p = "aa"
# s = "cbaebabacd"
# p = "abc"
print(checkAna(s, p))
