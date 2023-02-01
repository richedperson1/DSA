"""
URL : https://practice.geeksforgeeks.org/problems/pythagorean-triplet3018/1

"""


def polygon(arr):
    dist = {}
    for num in arr:
        local = num*num
        dist[local] = 1

    n = len(arr)
    for ind1 in range(n):
        for ind2 in range(ind1+1, n):
            b2 = arr[ind1]**2
            c2 = arr[ind2]**2
            if b2+c2 in dist:
                return True

    return False
