from typing import *
"""
URL : https://leetcode.com/problems/maximal-square/
"""


class Solution:
    maxi = 0

    def maximalSquare2(self, mat, i, j, dp):
        n = len(mat)
        m = len(mat[0])
        if i >= n or j >= m:
            return 0
        if dp[i][j] != -4:
            return dp[i][j]

        right = self.maximalSquare2(mat, i+1, j, dp)
        bottom = self.maximalSquare2(mat, i, j+1, dp)
        diagonal = self.maximalSquare2(mat, i+1, j+1, dp)
        if mat[i][j] == "1":
            ans = min(right, bottom, diagonal)+1
            dp[i][j] = ans
            self.maxi = max(self.maxi, ans)
            return ans
        else:
            dp[i][j] = 0
            return 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.maxi = 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-4 for i in range(m+1)] for j in range(n+1)]
        self.maximalSquare2(matrix, 0, 0, dp)
        return self.maxi**2


arr = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
       ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

final = Solution().maximalSquare(arr)
print(final)
