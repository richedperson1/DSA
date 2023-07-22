
from typing import List


class Solution:
    def minimizeTopSpeed(self, n :int, spells : List[int], trackLength:int) -> int:
        # code here
        low, high = 1, 10**9
        ans = high
        while low <= high:
            mid = (low+high)//2
            
            if self.canBePlaced(mid, spells, trackLength):
                ans = mid
                high = mid - 1
            
            else:
                low = mid + 1
        
        return ans
        
    def canBePlaced(self, k, spells, trackLength):
        currTrack = 0
        for i in range(1, len(spells)):
            diff = spells[i] - spells[i-1]
            if diff <= k:
                currTrack = diff * (k - diff) + diff * (diff + 1) / 2
            else:
                currTrack = k*(k+1)//2
            trackLength -= currTrack
            
        currTrack = k*(k+1)//2
        trackLength -= currTrack
        
        return trackLength <= 0
