"""
URL : https://leetcode.com/problems/optimal-partition-of-string
"""
from collections import defaultdict
string = "abaca"


# Recursive solution

"""
Time complexity : O(n)
Time complexity : O(n) Stack space
"""
final_ans = [1]


def count_unique(string, ind, dist):
    n = len(string)
    if ind >= n:
        return 0

    if string[ind] not in dist:
        dist += string[ind]
    else:
        final_ans[0] += 1
        dist = string[ind]

    return count_unique(string, ind+1, dist)


dist = ""
count_unique(string, 0,  dist)
print(final_ans)

# Iterative solution


"""
Time complexity : O(n)
Time complexity : O(1) 
"""


def count_unique_iter(string):
    res = 1
    dist = {}
    for char in string:
        if char in dist:
            res += 1
            dist = {}

        dist[char] = True

    return res


print(count_unique_iter(string))
