"""
Given an array arr of size n and an integer X. 
Find if there's a triplet in the 
array which sums up to the given integer X.

n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
True

Input:
n = 5, X = 10
arr[] = [1 2 4 3 6]
Output:
1


"""


def find3Numbers(arr, n, x):
    # Your Code Here
    arr = sorted(arr)
    for i in range(n):
        ind2 = i+1
        ind3 = n-1
        sumi = 0
        while ind2 < ind3:
            sumi = arr[i]+arr[ind2] + arr[ind3]
            if sumi == x:
                return True
            elif sumi > x:
                ind3 -= 1
            else:
                ind2 += 1
    return False


# Find Missing And Repeating.py
arr = sorted(list(map(int, "890 479 884 926 266 261 46 779 822 856 521 928 774 135 252 676 337 335 2 738 311 975 591 357 72 81 936 146 283".split())))
k = 647
# print(arr)
print(find3Numbers(arr, len(arr), k))
