"""
URL : https://leetcode.com/problems/sort-characters-by-frequency/
"""
from collections import Counter

"""
Time complexity : O(n)
space complexity: O(k)

required space for counter is only 26 because of 
"""


def sortbyFreq(string):
    final = Counter(string)
    double = sorted(final.items(), key=lambda item: item[1], reverse=True)
    print(list(final))
    form = ""
    for key, val in double:
        form += key*val
    return form


def frequencySort(s: str) -> str:
    from collections import Counter
    ansCounter = Counter(s)
    ans = ""
    for k, v in ansCounter.most_common():
        ans += k*v
    return ans


string = "aabbcccdA"
final = sortbyFreq(string)
final2 = frequencySort(string)
print(final)
print(final2)
