import sys


"""
! url : https://leetcode.com/problems/roman-to-integer/
"""
"""
! Time complexity : O(n)
! Space complexity : O(1)
"""

def romanToInt( s: str) -> int:
    dist = {
        "I":1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    prev = sys.maxsize

    newNum = 0
    for num in s:
        char = dist[num]
        if char>prev:
            newNum-=prev
            newNum += (char-prev)
            prev = (char-prev)
        else:
            newNum += char
            prev = char

    return newNum
        

roman = "MCMXCIV"



print(romanToInt(roman))