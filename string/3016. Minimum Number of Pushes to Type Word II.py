from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        dist = Counter(word)

        keys = sorted(dist,key = lambda x:dist[x],reverse=True)
        print(dist)
        first = 0

        total = 0
        for  ind,key in enumerate(keys):

            if ind%8==0:
                first+=1

            total+= (dist[key]*first)
        
        return total
    
obj = Solution()

string = "aabbccddeeffgghhiiiiii"


print(obj.minimumPushes(string))