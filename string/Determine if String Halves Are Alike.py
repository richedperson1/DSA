"""
URL : https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""

"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        total = len(s)
        first = total//2
        fstV = 0
        sndV = 0
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(first):
            checkF = s[i]
            checkS = s[i+first]
            if checkF in vowel:
                fstV += 1
            if checkS in vowel:
                sndV += 1

        return sndV == fstV

    def halvesAreAlike2(self, S: str) -> bool:
        mid, ans = len(S) // 2, 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(mid):
            if S[i] in vowels:
                ans += 1
            if S[mid+i] in vowels:
                ans -= 1
        return ans == 0
