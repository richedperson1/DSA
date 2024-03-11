from collections import defaultdict,Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        count = defaultdict(int)

        maxi = 0
        letter = ""
        for ind,data in enumerate(s):
            local_count = count.get(data,0)+1
            count[data] = local_count
            if local_count>maxi:
                letter = data
                maxi   = local_count
        total = 0
        for data in count:
            if data==letter:
                continue
            total+= count[data]
        
        if (count[letter]-total)>1:
            return  ""
        
        final_out = [""]*len(s)
        size      = len(s)
        ind = 0
        for maxi_index in range(count[letter]):
            final_out[ind] = letter
            ind+=2
        # print(final_out)
        for key,value in count.items():
            if key!=letter:
                for val in range(value):
                    if ind>=len(s):
                        ind = 1
                    final_out[ind] = key
                    ind+=2
        return "".join(final_out)
    
    def reorganizeString2(self,string:str)->str:
        
        count = Counter(string)
        
        count_key = [(-cnt,key) for cnt,key in count.items()]
        
        heapq.heapify(count_key)
        
        prev = None
        res  = ""
        
        while count_key or prev:
            if prev and not count_key:
                return  ""
            cnt,key = heapq.heappop(count_key)
            res    += key
            cnt    += 1
            
            if prev:
                heapq.heappush(prev)
                prev = None
            
            if cnt!=0:
                prev = [cnt,key]
        
        return res
            