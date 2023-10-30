"""
! URL : https://www.codechef.com/problems/NDIFFPAL
"""

size = int(input())

"""
Time complexity : O(n)
Time complexity : O(n)
"""
for _ in range(size):
    
    testCase = int(input())
    
    newForm = ''
    curr = 0
    
    for ind in range(testCase):
        if curr> ord('z')%97:
            curr = 0
        newForm += chr(curr+97)
        curr+= 1 
        
    print(newForm)