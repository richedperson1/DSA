"""
URL : https://leetcode.com/problems/longest-common-prefix/
"""


strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]


"""
! Time complexity : O(n^2)
! Space complexity : O(1)
"""
def longCommonPrefix(arr):
    word = min(arr,key=len)

    form = ""
    for ind,char in enumerate(word):
        flag = True
        for arrw in arr:
            if arrw[ind]!=char:
                flag = False
                
        if flag:
            form +=char
        else:
            break

    return form


"""
! Time complexity : O(n.log(n))
! Space complexity : O(1)
"""

def longCommonPrefixOptimize(arr):
    arr.sort()
    
    size = min(len(arr[0]),len(arr[-1]))
    form = ""
    for ind in range(size):
        if arr[0][ind]==arr[-1][ind]:
            form+=arr[0][ind]
        else:
            return form
    return form

print(longCommonPrefix(strs))
print(longCommonPrefixOptimize(strs))