import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.graph import Graph as G

def bfs(g: G, source, sink, parent):
    queue = []

    visited = [False for _ in g.v]

    queue.append(source)
    visited[source - 1] = True

    while queue != []:
        u = queue.pop(0)

        for v in range(1, len(g.adjacency_matrix[u - 1]) + 1):
            if (not visited[v - 1]) and g.adjacency_matrix[u - 1][v - 1] > 0:
                queue.append(v)
                parent[v - 1] = u
                visited[v - 1] = True

                if v == sink:
                    return True
                
    return False


def ford_fulkerson(g: G, source: int, sink: int) -> int:
    parent = [ -1 for _ in g.v]

    max_flow = 0

    while bfs(g, source, sink, parent):
        curr_flow = float('inf')
        t = sink

        while t != source:
            curr_flow = min(curr_flow, g.adjacency_matrix[parent[t - 1] - 1][t - 1])
            t = parent[t - 1]
        
        max_flow += curr_flow

        v = sink

        while v != source:
            u = parent[v - 1]
            g.adjacency_matrix[u - 1][v - 1] -= curr_flow
            g.adjacency_matrix[v - 1][u - 1] += curr_flow
            v = u
    
    return max_flow

def main():
    vertices = [1, 2, 3, 4, 5, 6]
    edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 2), (3, 5), (4, 3), (4, 6), (5, 4), (5, 6)]
    weights = [16, 13, 10, 12, 4, 14, 9, 20, 7, 4]
    directed = True

    source = 1
    sink = 6
    
    g = G(vertices, edges, weights, directed)

    print('\nInput network flow adjacency matrix\n')

    print(g)

    print(f'Source - {source}, Sink - {sink}')
    
    print('\nFord-Fulkerson\'s Algorithm to find max flow\n')
    
    max_flow = ford_fulkerson(g, source, sink)

    print(f'Maximum possible flow - {max_flow}')

if __name__ == "__main__":
    main()