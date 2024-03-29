from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        visit = {}

        adj = defaultdict(set)
        
        for ind in range(1,N):
            second = alien_dict[ind]
            first  = alien_dict[ind-1]
            for fc,sc in zip(first,second):
                if fc!=sc:
                    adj[ord(fc)-97].add(ord(sc)-97)
                    
                    # if ord(sc)-97 not in adj:
                    #     adj[ord(sc)-97] = set()
                        
                    
                    break
        
        indegree = defaultdict(int)
        
        for vtx in adj:
            for out in adj[vtx]:
                indegree[out]+=1
                
        
        stack = deque([])
        print("adj",len(adj))
        print("adj",adj)
        for key in adj:
            if indegree[key]==0:
                stack.append(key)
        
        final = ""
        while len(stack)>0:
            node = stack.popleft()         
            final+= chr(97+node)
            
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child] ==0:
                    stack.append(child)
        return final
    
    

arr = list(map(str,"bhhb blkbggfecalifjfcbkjdicehhgikkdhlachlgbhji cfjjhcifladadbgcleggjgbcieihabcglblflgajgkejccj dlgdhiha ehggedljjhfldcajeceaeehkalkfeidhigkifjl gdalgkblahcldahledfghjb geldbblaaflegjhlfjlgblfbdc ibjceciedbiilkjliijgklcgliaeeic jcebjkfgfibfckfiikklecihik jdkcabjjjckgdblkljf jijlbjbliigkffhkchkclkhafbiiiblcglhfjkflbjjkih kfd lhdgidialgabfklffahiihceflebfidl".split()))

n = len(arr)
k = 12
obj = Solution()
result = obj.findOrder(arr,n,k)

print(len(result),result)
