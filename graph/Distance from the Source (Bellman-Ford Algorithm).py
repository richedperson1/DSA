"""
https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
"""

"""
The function `bellman_ford` implements the Bellman-Ford algorithm to find the shortest path from a
source vertex to all other vertices in a weighted directed graph.

param v: The parameter `v` represents the number of vertices in the graph

param edges: The "edges" parameter is a list of tuples representing the edges in the graph. Each
tuple contains three elements: the source vertex, the destination vertex, and the weight of the edge

param s: The parameter "s" represents the source vertex from which the shortest paths are
calculated

return: The function `bellman_ford` returns a list of distances from the source vertex `s` to all
other vertices in the graph.
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