from graph import Graph as G

def argmin(d: list, R: set):
    min_vertex = None
    min_distance = float('inf')
    for vertex, distance in enumerate(d):
        if vertex + 1 in R:
            continue
        if distance < min_distance:
            min_distance = distance
            min_vertex = vertex

    return min_vertex + 1 # Since vetices are 1-indexed.

def djikstras(g: G, source: int):
    d = [
        (
            g.adjacency_matrix[source - 1][v - 1]
            if g.adjacency_matrix[source - 1][v - 1] != 0
            else float("inf")
        )
        for v in g.v
    ]
    d[source - 1] = 0

    R = set()
    R.add(source)

    while len(R) < len(g.v):
        u = argmin(d, R)
        R.add(u)

        for vertex in g.v:
            if vertex != source and vertex + 1 not in R and g.adjacency_matrix[u - 1][vertex - 1] != 0:
                d[vertex - 1] = min(d[u - 1] + g.adjacency_matrix[u - 1][vertex - 1], d[vertex - 1])

    return d

def main():
    vertices = [1, 2, 3, 4]
    edges = [
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (3, 4),
    ]
    weights = [3, 6, 2, 9, 3]

    g = G(vertices, edges, weights)

    print("Graph adjacency matrix: \n")
    print(g)

    source = 1
    min_distance = djikstras(g, source)

    print(
        f"\nFinding shortest distance from source {source} to all vertices using Djikstras Algorithm\n"
    )

    print(min_distance)

if __name__ == "__main__":
    main()
