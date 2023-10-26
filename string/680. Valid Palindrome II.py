"""

! URL : https://leetcode.com/problems/valid-palindrome-ii/

"""
from collections import Counter
def validPalim(string):
    count = Counter(string)
    oddNum = 0
    for key,val in count.items():
        if val&1==1:
            oddNum+=1

    if oddNum<=2:
        return True
    return False


string = "aba"

print(validPalim(string))