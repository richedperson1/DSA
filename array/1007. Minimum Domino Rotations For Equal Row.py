"""
! URL : https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
"""

from typing import List
"""
Time complexity : O(n)
Space complexity : O(7)
"""
def minDominoRotations( tops: List[int], bottoms: List[int]) -> int:
    dist = {}

    size = len(tops)
    for ind in range(size):
        first,second = tops[ind],bottoms[ind]

        dist[first] = dist.get(first,0)+1
        dist[second] = dist.get(second,0)+1

    maxi = 0
    for key, val in dist.items():
        if val>=size:
            maxi = key
            break

    if maxi==0:
        return -1

    topCheck = 0
    bottomCheck = 0
    for ind in range(size):
        # Top Check
        if tops[ind]==maxi:
            pass
        else:
            if bottoms[ind]==maxi:
                bottomCheck+=1
            else:
                return -1

        if bottoms[ind]==maxi:
            pass
        
        else:
            if tops[ind]==maxi:
                topCheck+=1
            else:
                return -1

    return min(topCheck,bottomCheck)
    
"""
Time complexity : O(n)
Space complexity : O(1)
"""

def minDominoRotationsOptimize(tops,bottoms):

    for ind in range(1,7):
        if all(ind==first or ind==second for first ,second  in zip(tops,bottoms)):
            return min(len(tops)-tops.count(ind),len(bottoms)-bottoms.count(ind))
        
    return -1
tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]

print(minDominoRotationsOptimize(tops,bottoms))
print(minDominoRotations(tops,bottoms))