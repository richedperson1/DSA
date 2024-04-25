from collections import defaultdict


def topologicalSort(grid,v):
    ans = []
    visit = defaultdict(bool)
    # isPath = defaultdict(bool)

    def dfs(node):
        # isPath[node] = 1
        visit[node] = 1
        childs = grid[node]
        for child in childs:
            if not visit[child]:
                final = dfs(child)
                if final:
                    return True
                
            # elif isPath[child]:
            #     return True
        
        # isPath[node] = 0
        ans.append(node)
        return False

    for vtx in range(v):
        if visit[vtx]==False:
            dfs(vtx)
    return ans
grid = [[1,4],[2],[],[],[5],[1]]

print(topologicalSort(grid,6))