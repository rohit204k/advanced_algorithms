from graph import Graph as G

def prims(g: G):
    S = set()
    V = set(g.v)

    edges = sorted(g.e.items(), key=lambda item: item[1])

    mst_edges = set()

    S.add(g.v[0])
    while S!=V:
        for edge, weight in edges:
            if edge[0] in S and edge[1] not in S:
                mst_edges.add(edge)
                S.add(edge[1])
    
    return mst_edges


def main():
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)]
    weights = [1, 4, 3, 2, 5]

    g = G(vertices, edges, weights)

    print('\nFinding MST using Prims Algorithm\n')

    print('Graph adjacency matrix: \n')
    print(g)
    mst_edges = prims(g)

    print('MST has the following edges')
    print(mst_edges,'\n')

if __name__  == '__main__':
    main()