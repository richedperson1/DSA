from math import ceil ,floor

"""
! URL : https://leetcode.com/problems/count-good-numbers/
"""

def countGoodNumbers( n: int) -> int:
    return (pow(5,ceil(n/2),1000_000_007) * pow(4,floor(n/2),1000_000_007))% 1000_000_007
