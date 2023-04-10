"""
URL : https://leetcode.com/problems/boats-to-save-people/
"""

arr = [3, 2, 2, 1]
limit = 3


def boat_save(arr, ind, sumi, total):
    n = len(arr)
    if ind >= n:
        return 1
    if sumi == total:
        return 1

    inc = 0
    if sumi+arr[ind] <= total:
        inc = boat_save(arr, ind+1, sumi+arr[ind], total)
        return inc
    else:
        exc1 = boat_save(arr, ind+1, 0, total)
        exc2 = boat_save(arr, ind+1, sumi, total)
        return min(exc1, exc2)+1


print(boat_save(arr, 0, 0, limit))
