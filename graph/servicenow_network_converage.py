from collections import defaultdict
import bisect
from collections import defaultdict

class Solution1:
    def satelliteCoverage(self, arr, query):
        delta = defaultdict(int)
        for start, end in arr:
            delta[start] += 1
            delta[end + 1] -= 1
        
        sorted_points = sorted(delta.keys())
        p = defaultdict(int)
        coverage = 0
        prev = None
        
        for point in sorted_points:
            if prev is not None:
                start = prev
                end = point - 1
                if start <= end:
                    cnt = coverage
                    p[cnt] += end - start + 1
            coverage += delta[point]
            prev = point
        
        sorted_x = sorted(p.keys())
        if not sorted_x:
            return [0] * len(query)
        
        values = [p[x] for x in sorted_x]
        st = self.SegmentTree(values)
        
        res = []
        for q_low, q_high in query:
            left = bisect.bisect_left(sorted_x, q_low)
            right = bisect.bisect_right(sorted_x, q_high) - 1
            if left > right:
                res.append(0)
            else:
                max_val = st.query(left, right)
                res.append(max_val)
        
        return res
    
    class SegmentTree:
        def __init__(self, data):
            self.n = len(data)
            if self.n == 0:
                self.size = 0
                self.tree = []
                return
            self.size = 1
            while self.size < self.n:
                self.size <<= 1
            self.tree = [0] * (2 * self.size)
            for i in range(self.n):
                self.tree[self.size + i] = data[i]
            for i in range(self.size - 1, 0, -1):
                self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
        
        def query(self, l, r):
            if self.size == 0:
                return 0
            res = -float('inf')
            l += self.size
            r += self.size
            while l <= r:
                if l % 2 == 1:
                    res = max(res, self.tree[l])
                    l += 1
                if r % 2 == 0:
                    res = max(res, self.tree[r])
                    r -= 1
                l >>= 1
                r >>= 1
            return res if res != -float('inf') else 0



class Solution:
    def satelliteCoverage(self, arr, query):
        coverage_cnt = defaultdict(int)
        for start, end in arr:
            for point in range(start, end + 1):
                coverage_cnt[point] += 1

        p = defaultdict(int)
        for cnt in coverage_cnt.values():
            p[cnt] += 1
            

        res = []
        for q_low, q_high in query:
            max_px = 0
            for x in range(q_low, q_high + 1):
                
                if x in p:
                    max_px = max(max_px, p[x])
            res.append(max_px)
        
        return res


class Solution:
    def satelliteCoverage(self, arr, query):
        coverage_cnt = defaultdict(int)
        for start, end in arr:
            for point in range(start, end + 1):
                coverage_cnt[point] += 1

        p = defaultdict(int)
        for cnt in coverage_cnt.values():
            p[cnt] += 1
        
        cum_sum = {}
        total = 0
        for data in range(min(p),max(p)+1):
            total+= p.get(data,0)
            cum_sum[data] = total
        res = []
        for q_low, q_high in query:
            max_px =cum_sum.get(q_high,total)- cum_sum.get(q_low,total)
            res.append(max_px)
        
        return res





# Example usage:
arr = [[2, 3], [3, 4], [5, 5], [3, 4]]
queries = [[1, 2], [3, 4]]

arr = [[3,4],[2,3],[5,7]]
queries = [[1, 3], [3,3]]

arr = [[1, 2], [2, 3], [2, 2], [2, 4]]
query = [[1, 2], [2, 3]]

obj = Solution1()
print(obj.satelliteCoverage(arr, queries))  # Output: [2, 1]
