"""
URL : https://leetcode.com/problems/find-the-difference-of-two-arrays/
"""

"""
Method 1

Space Complexity : 
"""


def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    dist1 = {}
    dist1 = dist1.fromkeys(nums1, True)
    dist2 = {}.fromkeys(nums2, True)

    ans = [[], []]
    for lst1 in nums1:
        if dist2.get(lst1, 0) == 0:
            dist2[lst1] = True
            ans[0].append(lst1)

    for lst2 in nums2:
        if dist1.get(lst2, 0) == 0:
            dist1[lst2] = True
            ans[1].append(lst2)
    return ans


"""
Method 2 
"""


def findDifference2(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return [nums1-nums2, nums2-nums1]
