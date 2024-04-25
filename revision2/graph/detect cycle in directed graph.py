from collections import defaultdict

def checkCycle(adj,v):

    def dfs(node):
        visit[node] = True

        childS = adj[node]

        for child in childS:
            if child not in visit:
                ans = dfs(child)
                if ans==True:
                    return True
                
            elif child in inSide:
                return True
            
        return False

    visit = defaultdict(bool)

    inSide = set()
    for vtx in range(v):
        if vtx not in visit:
            inSide.add(vtx)
            ans = dfs(vtx)
            if ans==True:
                return True
            inSide.remove(vtx)
        if vtx in inSide:
            return True
        
    return False