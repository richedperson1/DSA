from queue import PriorityQueue

def dijkstraAlgo(src,adj,v):

    pq = PriorityQueue()
    dist = [float("inf")]*(v)
    dist[src] = 0

    pq.put((0,src))

    while not pq.empty():
        weight,node = pq.get()

        for child in adj[node]:

            localWeight = weight+child[-1]
            if localWeight < dist[child[0]]:
                pq.put((localWeight,child[0]))
                dist[child[0]] = localWeight

    return dist


V = 3
E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]

print(dijkstraAlgo(0,adj,V))