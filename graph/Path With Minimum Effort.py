from queue import PriorityQueue

def MinimumEffort( a):

    pq = PriorityQueue()
    
    sr,sc = 0,0
    
    pq.put((0,(0,0)))
    
    n,m = len(a),len(a[0])
    dist = [[float('inf')]*(m) for ind in range(n)]
    dire = [[-1,0],[1,0],[0,1],[0,-1]]
    
    dist[0][0] = 0
    while not pq.empty():
        nodeWeight,current = pq.get()
        row,col = current
        if row+1==n and col+1==m:
            return dist
        for dr,dc in dire:
            newR,newC = row+dr,col+dc
            if 0 <= newR < n and 0 <= newC < m :
                effort = max(abs(a[row][col]-a[newR][newC]),nodeWeight )
                
                if effort<dist[newR][newC]:
                    pq.put((effort,(newR,newC)))
                    dist[newR][newC] = effort
                
                
    return dist

grid = [[1,2,3],
        [3,3,2],
        [5,3,5]]

print(MinimumEffort(grid)) 