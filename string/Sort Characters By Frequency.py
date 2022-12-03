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


"""
Bucket sort technique
"""


"""
Time complexity : O(n)
space complexity : O(n)
"""


def freqSort(s):
    final = Counter(s)
    n = len(final)
    bucket = [[] for i in range(n+1)]
    for word, repeat in final.items():
        bucket[repeat].append(word)

    finalAns = ""
    for num in range(n, 0, -1):
        for letter in bucket[num]:
            finalAns += letter*num
    return finalAns


string = "aabbcccdA"
final = sortbyFreq(string)
final2 = frequencySort(string)
print(freqSort(string))
print(final)
print(final2)
