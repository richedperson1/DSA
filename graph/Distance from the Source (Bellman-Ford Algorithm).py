"""
https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
"""

def bellman_ford( v, edges, s):
    #code here

    dist = [int(1e8)]*v
    dist[s] = 0
    
    for ind in range(v-1):
        for src,dst,weight in edges:
            if dist[src]+weight<dist[dst]:
                dist[dst] = dist[src]+weight
                

    for src,dst,weight in edges:
        if  dist[src]+weight<dist[dst]:
            return [-1]
            
    return dist