from collections import defaultdict,deque
class Solution:
    def findOrder(self, n, m, arr):
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for ind in range(m):
            v,u = arr[ind]
            adj[u].append(v)
            indegree[v]+=1
        
        
        pq = deque()
        
        for degree in range(n):
            if indegree.get(degree,0)==0:
                pq.append(degree)
        result = []
        while pq:
            node = pq.popleft()
            result.append(node)
            for child in adj[node]:
                indegree[child]-=1
                if indegree[child]<=0:
                    pq.append(child)
        
        return result if len(result)==n else []
    

arr  = [[1, 0],
               [2, 0],
               [3, 1],
               [3, 2]]
arr = [[3,10],[11,12],[11,13],[2,9],[7,8],[0,6]]
# arr = [[3,3],[1,1]]
obj = Solution()
m = len(arr)
n = 17

print(obj.findOrder(n,m,arr))
