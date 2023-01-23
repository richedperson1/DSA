"""
URL : https://leetcode.com/problems/word-break/

"""

"""
Time complexity : O(k^n*n)
space complexity : O(n)
"""


def check(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2:
        return False
    for ind in range(n1):
        if s1[ind] != s2[ind]:
            return False
    return True


def wordBreak(string, start, wordDict):
    if len(string) <= start:
        return True

    final = False
    for word in wordDict:
        size = len(word)
        subString = string[start:start+size]
        if check(subString, word):
            local = wordBreak(string, start+size, wordDict)
            final = final or local

    return final


def wordBreakDP(string, start, wordDict, dp):
    if len(string) <= start:
        return True

    if dp[start] != -1:
        return dp[start]
    final = False
    for word in wordDict:
        size = len(word)
        subString = string[start:start+size]
        if check(subString, word):
            local = wordBreakDP(string, start+size, wordDict, dp)
            final = final or local

    dp[start] = final
    return final


def wordBreakTabDP(string, wordDict):
    n = len(string)
    dp = [False]*(n+2)
    dp[n] = True
    dp[n+1] = True
    for ind in range(n-1, -1, -1):
        for word in wordDict:
            nW = len(word)
            subString = s[ind:ind+nW]
            if (ind+nW <= n) and subString == word:
                dp[ind] = dp[ind+nW]
            if dp[ind]:
                break
    return dp[0]


wordDict = ["leet", "ode", "c.2"]
s = "leetc.2ode"
n = len(s)
print(wordBreak(s, 0, wordDict))
dp = [-1]*(n+1)
print(wordBreakDP(s, 0, wordDict, dp))
print(wordBreakTabDP(s,  wordDict))
