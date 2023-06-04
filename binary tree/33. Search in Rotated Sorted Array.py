"""
URL : https://leetcode.com/problems/search-in-rotated-sorted-array/
"""


def search( arr: list[int], target: int) -> int:
    low , high = 0 , len(arr)-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid]==target:
            return mid

        else:
            if arr[0]<=arr[mid]:
                if arr[mid]>=target and arr[low]<=target:
                    high = mid-1
                else:
                    low = mid+1

            else:
                if arr[mid]<=target and arr[-1]>=target:
                    low = mid+1
                else:
                    high = mid-1

    return  -1