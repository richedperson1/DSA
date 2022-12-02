"""
URL : https://leetcode.com/problems/determine-if-two-strings-are-close/
"""
from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    dist1 = {}
    dist2 = {}
    for letter in word1:
        if letter in dist1:
            dist1[letter] += 1
        else:
            dist1[letter] = 1

    for letter in word2:
        if letter not in dist1:
            return False
        if letter in dist2:
            dist2[letter] += 1
        else:
            dist2[letter] = 1

    final = sorted(list(dist1.values()))
    for letter in dist2:
        if dist2[letter] not in final:
            return False

    ans2 = Counter(Counter(word1).values())
    print(ans2)
    return(list(dist2.values()) == list(dist1.values()))


w1 = "aaabbbbccddeeeeefffff"
w2 = "aaaaabbcccdddeeeeffff"
w1 = "abc"
w2 = "bca"
print(closeStrings(w1, w2))
