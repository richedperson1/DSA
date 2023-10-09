"""
! URL : https://leetcode.com/problems/consecutive-numbers-sum/
"""


def consecutiveNum(n):
    dist = {0:0}
    curr = 0
    for data in range(0,n+1):
        curr+=data
        remain = curr-n
        if remain in dist:
            return data-dist[remain]
        
        dist[curr] = data

    


print(consecutiveNum(15))
