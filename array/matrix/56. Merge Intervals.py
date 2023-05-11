"""
url : https://leetcode.com/problems/merge-intervals/
"""
from typing import List

class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key = lambda x : x[0])
        output = [arr[0]]
        for start, end in arr:
            lastEnd = output[-1][-1]
            if start<=lastEnd:
                lastEnd = max(lastEnd,end)
                output[-1][-1] = lastEnd

            else:
                output.append([start,end])
        
        return output