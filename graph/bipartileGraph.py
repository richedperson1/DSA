from collections import defaultdict, deque

class Solution:
    def isBipartite(self, V, adj):
        visit = defaultdict(bool)

        def bfs(src):
            queue = deque([src])
            visit[src] = 0
            while queue:
                element = queue.popleft()

                for child in adj[element]:
                    if not visit.get(child, False):
                        visit[child] = ~visit[element]
                        queue.append(child)
                    elif visit[child] == visit[element]:
                        return False
            return True

        visit = defaultdict(bool)
        for v in range(V):
            if bfs(v)==False:
                return False
        return True

    def isBipartiteD(self, V, adj):
        visit = defaultdict(bool)

        def dfs(src,color):
            visit[src] = color
            for child in adj[src]:
                if child not in visit:
                    ans = dfs(child,1^color)
                    if ans==False:
                        return False
                elif visit[child] == visit[src]:
                    return False
            return True

        visit = defaultdict(bool)
        for v in range(V):
            if v not in visit :
                if dfs(v,0)==False:
                    return False
        return True      

arr = '''0 2
0 3
1 3
2 3'''
grid = [[2], [2, 3], [0, 1, 3], [1, 2]]

obj = Solution()
print(obj.isBipartiteD(4,grid))
# } Driver Code Ends