from collections import defaultdict
 
def getCount(N, s):
    dist = defaultdict(int)
    ans = 0
    for ind,data in enumerate(box):
        mask = 0
        for char in box[ind]:
            local = 1<<(ord(char)-ord("a"))
            mask^=local
        
        ans+=dist[mask]
        dist[mask]+=1
        for ind in range(26):
            mask^=1<<ind
            ans+= dist[mask]
            mask ^= 1<<ind
    
    return ans
 




box = ["aaaa", "abba", "ccc", "caa", "cbba", "acaac", "bcb"]
n = len(box)
print(getCount(n,box))
box = ["bbcb", "abccc", "abc"]
n = len(box)
result = getCount(n,box)
print(result) 