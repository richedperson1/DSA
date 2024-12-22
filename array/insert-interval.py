
class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        new_result = []
        first = 1
        for interval in intervals:
            if interval[1]<newInterval[0]:
                new_result.append(interval)
                
            elif interval[0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0],interval[0])
                newInterval[1] = max(newInterval[1],interval[1])
                if first==1:
                    new_result.append(newInterval)
                else:
                    new_result[-1] = newInterval
                first = 0
                
                
            else:
                new_result.append(interval)
        return new_result
    
intervals = [[1,3], [4,5], [6,7], [8,10]]
newInterval = [5,6]

obj = Solution()

print(obj.insertInterval(intervals,newInterval))


