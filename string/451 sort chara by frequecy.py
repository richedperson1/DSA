from collections import defaultdict


"""
Url : https://leetcode.com/problems/sort-characters-by-frequency/
"""

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)

        for char in s:
            freq[char]+=1

        
        freq = sorted(freq.items(),key = lambda x:x[1],reverse = True)

        form = ""
        for data in freq:
            form += data[0]*data[1]

        return form