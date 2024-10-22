class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        """Given a string s, return the maximum number of unique substrings that the given string can be split into.

            You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique."""
        def max_substring(ind):
            if ind == len(s):
                return 0

            ans = 0
            for i in range(ind, len(s)):
                if s[ind:i+1] not in seen:
                    seen.add(s[ind:i+1])
                    ans = max(ans, 1 + max_substring(i+1))
                    seen.remove(s[ind:i+1])
            return ans

        seen = set()
        return max_substring(0)
    
    
result = Solution()

print(result.maxUniqueSplit("ababccc"))