import os
import sys
import random
from copy import copy
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_structures.graph import MultiGraph as G

def kargers_min_cut(g: G):
    v = len(g.v)

    while v>2:
        random_edge = random.choice(list(g.e.keys()))

        g.e.pop(random_edge, False)
        g.adjacency_matrix[random_edge[0] - 1][random_edge[1] - 1] = 0
        g.adjacency_matrix[random_edge[1] - 1][random_edge[0] - 1] = 0

        max_v, min_v = max(random_edge), min(random_edge)

        for vertex in range(1, len(g.v) + 1):
            if vertex == min_v or g.adjacency_matrix[max_v - 1][vertex - 1] == 0:
                continue
            else:
                g.e[(min(min_v, vertex), max((min_v, vertex)))] = g.e.get((min(min_v, vertex), max((min_v, vertex))), 0) +  g.e.get((min(max_v, vertex), max((max_v, vertex))))
                g.adjacency_matrix[min_v - 1][vertex - 1] += g.adjacency_matrix[max_v - 1][vertex - 1]
                g.adjacency_matrix[vertex - 1][min_v - 1] += g.adjacency_matrix[vertex - 1][max_v - 1]

                g.e.pop((min(max_v, vertex), max((max_v, vertex))), False)
                g.adjacency_matrix[max_v - 1][vertex - 1] = 0
                g.adjacency_matrix[vertex - 1][max_v - 1] = 0

        v -= 1


    return g
        

def main():
    vertices = [1, 2, 3, 4, 5, 6, 7]
    edges = [(1, 2), (1, 4), (2, 4), (2, 3), (3, 5), (3, 6), (3, 7), (4, 5), (5, 6), (6, 7), (5, 7)]
    
    g = G(vertices, edges)

    print('Karger\'s Min Cut Algorithm\n')
    print('Input Graph - ')
    print(g)

    g_ = kargers_min_cut(g)

    print(f'Min Cut obtained in 1 run - {list(g_.e.values())[0]}\n')
    
    r = 30
    print(f'Repeating algorithm {r} times')

    results = []
    for _ in range(r):
        g = G(vertices, edges)
        g_ = kargers_min_cut(g)
        results.append(list(g_.e.values())[0])

    print(f'Repeated run results -\n{results}\n')
    print(f'Min Cut after repeated runs - {min(results)}')

if __name__ == "__main__":
    main()