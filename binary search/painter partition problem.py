"""
! URL : https://www.interviewbit.com/problems/painters-partition-problem/
"""

class Solution:

    def paint(self, A, B, C):
        if len(C) == A:
            return (max(C) * B) % 10000003

        def isPossible(mid, pNum):
            wallPaint = 0
            painter = 1
            for ind, data in enumerate(C):
                if data > mid:
                    return False

                elif data + wallPaint <= mid:
                    wallPaint += data

                else:
                    painter += 1
                    if painter > pNum:
                        return False

                    wallPaint = data

            return True

        low, high = min(C), sum(C)
        ans = -1
        while low <= high:
            mid=(low+high) // 2
            if isPossible(mid, A):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return (ans * B) % 10000003
