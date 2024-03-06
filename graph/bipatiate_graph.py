from collections import deque
class Solution:
    def isBipartite(self,v,graph):
        rev = {0:1,1:0}
        color = {}
        def bfs(start):
            color[start] = 0
            stack = deque([start])
            while len(stack)>0:
                node = stack.popleft()
                nColor = color.get(node)
                cColor = rev.get(nColor)
                
                for child in graph[node]:
                    if child==node:
                        continue
                    elif color.get(child,-1)==-1:
                        color[child] = cColor
                        stack.append(child)
                    elif cColor!=color.get(child):
                        return False
        
        for data in range(len(graph)):
            if color.get(data,-1)==-1 and  bfs(data)==False:
                return False
        return True
    

arr = [[1], [0, 2], [1]]
v = 2
obj = Solution()
print(obj.isBipartite(v,arr))
                