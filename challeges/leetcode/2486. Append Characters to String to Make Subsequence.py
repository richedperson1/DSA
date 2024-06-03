from collections import deque,defaultdict
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_dist = defaultdict(lambda : deque())

        for ind,data in enumerate(s):
            s_dist[data].append(ind)

        
        last_ind = -1
        total = 0
        for t_data in t:
            # try:
                if len(s_dist.get(t_data,[]))>0 and last_ind<s_dist[t_data][0]:
                    last_ind = s_dist[t_data][0]
                    s_dist[t_data].popleft()
                else:
                    return len(t)-total
                
                total+=1

        return len(t)-total
    
    
obj = Solution()
s = "cdoaching"
t = "coding"
print(obj.appendCharacters(s,t))