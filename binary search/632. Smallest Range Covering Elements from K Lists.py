"""
! URL : https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
"""

def smallestRange(arr):
    arrRange = []
    gMini = float("inf")
    gMaxi = -float("inf")
    for data in arr:
        mini = data[0]
        maxi = data[-1]
        arrRange.append([mini,maxi])

        gMini = min(gMini,mini)
        gMaxi = max(gMaxi,maxi)

    
    