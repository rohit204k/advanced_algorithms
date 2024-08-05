from graph import Graph as G

def kruskals(g: G):
    mst_edges = set()
    cycle_check = {i: i for i in g.v}
    
    for edge, weight in sorted(g.e.items(), key=lambda item: item[1]):
        if cycle_check[edge[0]] != cycle_check[edge[1]]:
            mst_edges.add(edge)

            v1 = max(cycle_check[edge[0]], cycle_check[edge[1]])
            v2 = min(cycle_check[edge[0]], cycle_check[edge[1]])
            for v in cycle_check:
                if cycle_check[v] == v1:
                    cycle_check[v] = v2

        else:
            continue

    return mst_edges



def main():
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (2, 3), (1, 3), (3, 4), (4, 5)]
    weights = [1, 4, 3, 2, 5]

    g = G(vertices, edges, weights)

    print('\nFinding MST using Kruskal Algorithm\n')

    print('Graph adjacency matrix: \n')
    print(g)
    mst_edges = kruskals(g)

    print('MST has the following edges')
    print(mst_edges,'\n')

if __name__  == '__main__':
    main()