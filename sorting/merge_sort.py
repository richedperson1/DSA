"""
URL : https://practice.geeksforgeeks.org/problems/merge-sort/1
"""


def mergeSortAlgorithms(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSortAlgorithms(left)
        mergeSortAlgorithms(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining Element if present in left or right array

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = [1, 1, -1, 1, 2, 1, 2]
brr = arr.copy()
mergeSortAlgorithms(arr)
print(arr)
print(sorted(brr))
