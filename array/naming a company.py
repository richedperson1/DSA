"""
URL : https://leetcode.com/problems/naming-a-company/
"""


from collections import *


def swap(l1, l2):
    temp = l1
    l1 = l2[0]+l1[1:]
    l2 = temp[0]+l2[1:]
    return l1, l2


def distinctNames(ideas: list[str]) -> int:
    firstDict = defaultdict(set)

    for word in ideas:
        firstDict[word[0]].add(word[1:])

    ans = 0
    for chr1 in firstDict:
        for chr2 in firstDict:
            if chr1 == chr2:
                continue

            interset = 0
            for word in firstDict[chr2]:
                if word in firstDict[chr1]:
                    interset += 1

            ans += (len(firstDict[chr2])-interset) * \
                (len(firstDict[chr1])-interset)

    return ans


def distinctNames2(ideas: list[str]) -> int:

    finalDict = {}
    for word in ideas:

        finalDict[word] = True

    ans = 0
    firstLen = len(finalDict)
    size = len(ideas)
    for ind1 in range(size):
        for ind2 in range(size):
            firstW = arr[ind1]
            secondW = arr[ind2]
            w1, w2 = swap(firstW, secondW)
            if finalDict.get(w1, 0) == 0 and finalDict.get(w2, 0) == 0:
                ans += 1
            finalDict[w1+w2] = True
    return ans


arr = ["coffee", "donuts", "time", "toffee"]
print(distinctNames(arr))
