import sys


arr = [1, 2, 3, -2, 5]

# method 1 brute force approach
maxi = -sys.maxsize
# print(maxi)
curr = 0
for num in arr:
    curr = max(num, num+curr)
    maxi = max(maxi, curr)

print(maxi)
