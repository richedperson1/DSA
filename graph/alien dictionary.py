from collections import defaultdict
def findOrder(alien_dict, N, k):
    # adj = [[] for i in range(N)]
    # for ind in range(N-1):
    #     s1 = alien_dict[ind].lower()
    #     s2 = alien_dict[ind+1].lower()
        
    #     for char1,char2 in zip(s1,s2):
    #         if char1!=char2:
    #             l1,l2 = ord(char1)%97,ord(char2)%97
    #             # print(l1,l2)
    #             adj[l1].append(l2)
    #             break
    
    # # return(adj)

    adj = [[] for i in range(k)]
    for ind in range(N-1):
        s1 = alien_dict[ind].lower()
        s2 = alien_dict[ind+1].lower()
        
        for char1,char2 in zip(s1,s2):
            if char1!=char2:
                l1,l2 = ord(char1)%97,ord(char2)%97
                adj[l1].append(l2)
                break
    
    visit = defaultdict(bool)
    isPath = defaultdict(bool)
    ans = []
    def dfs(node):
        isPath[node] = 1
        visit[node] = 1
        childs = adj[node]
        for child in childs:
            if not visit[child]:
                final = dfs(child)
                if final:
                    return True
                
            elif isPath[child]:
                return True
        
        isPath[node] = 0
        ans.append(node)
        return False

    for vtx in range(k):
        if visit[vtx]==False:
            dfs(vtx)
        
    for ind,data in enumerate(ans):
        ans[ind] = chr(data+97)
    
    
    return ans[::-1]
N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]

print(findOrder(dict,N,K))