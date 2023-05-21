"""
URL : https://leetcode.com/problems/rotate-array/
"""

arr = [1,2,3,4,5,6,7]
k = 2
#  [5,6,7,1,2,3,4]
n = len(arr)

arr.reverse()
kk = k-1
ind= 0


while kk>ind:
    arr[kk],arr[ind] = arr[ind],arr[kk]
    kk-=1
    ind+=1


start = k
endInd= n-1 
while start<endInd:
    arr[start],arr[endInd] = arr[endInd],arr[start]
    start+=1
    endInd-=1
print(arr)