# Graph Class
# vertices: list of vertices (vertices are numbered from 1 and onwards.)
# edges: list of edges (each edge is a tuple of form (s,v), ex: (1,2))
# weights: list of weights in order pass in edges, defaults to None, which is 1 for all edges
# directed: True for directed graphs, False otherwise.

class Graph:
    def __init__(self, vertices, edges, weights=None, directed=False) -> None:
        self.v = vertices
        self.e = {}
        if weights is None:
            weights = [1] * len(edges)

        for i in range(len(edges)):
            self.e[edges[i]] = weights[i]

        self.adjacency_matrix = [[0] * len(self.v) for _ in range(len(self.v))]

        for (u, v), weight in self.e.items():
            self.adjacency_matrix[u - 1][v - 1] = weight
            if not directed:
                self.adjacency_matrix[v - 1][u - 1] = weight

    def __str__(self):

        matrix_str = "  " + " ".join(map(str, self.v)) + "\n"

        for i in range(len(self.v)):
            matrix_str += (
                str(self.v[i])
                + " "
                + " ".join(map(str, self.adjacency_matrix[i]))
                + "\n"
            )

        return matrix_str
