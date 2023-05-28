"""
URL : https://leetcode.com/problems/longest-consecutive-sequence/
"""

def countingProp(data,count,dist):

    if dist.get(data,-1)==-1:
        return 0

    if count.get(data,-1)!=-1:
        return count[data]

    ans = countingProp(data+1,count,dist)+1
    count[data] = ans
    return ans



def longestConsecutive( arr: list[int]) -> int:
    dist = {}
    for ind, data in enumerate(arr):
        dist[data] = 0

    long = 0
    count = {}
    for data in arr:
        find = data
        local = countingProp(find,count,dist)
        count[data] = local
        long = max(local,long)

    return long