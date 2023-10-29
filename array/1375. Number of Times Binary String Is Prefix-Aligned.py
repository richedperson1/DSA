"""
1375. Number of Times Binary String Is Prefix-Aligned
https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

"""


def numTimesAllBlue( flips: list[int]) -> int:

    currSum = 0
    ans = 0
    for ind,data in enumerate(flips):
        currSum+=data
        x = ind+1
        if currSum == (x*(x+1))//2:
            ans+=1
        
    return ans

