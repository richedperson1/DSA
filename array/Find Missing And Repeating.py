"""
Given an unsorted array Arr of size N of positive integers. 
One number 'A' from set {1, 2, …N} is missing and one number 'B' 
occurs twice in array. Find these two numbers.

Input 1:
N = 2
Arr[] = {2, 2}
Output 1: 2 1

Input 2:
N = 3
Arr[] = {1, 3, 3}
Output 2: 3 2

"""
# Method 1


def find_two(arr, n):
    arr = sorted(arr)
    ans = [0, 0]
    for i in range(n):
        if i+1 != arr[i]:
            ans[0] = i
        if arr[i] == arr[i+1]:
            ans[1] = arr[i]
    return ans


"""
Time complexity : O(n.log(n))
Space complexity: O(1)
"""

# Method 2


def findTwoElement(arr, n):
    dist = {}
    ans = [0, 0]
    for data in arr:
        if data in dist:
            ans[0] = data
        else:
            dist[data] = 1
    for i in range(1, n+1):
        if i not in dist:
            ans[1] = i
    return ans


"""
Time complexity : O(n)
Space complexity: O(n)
"""
