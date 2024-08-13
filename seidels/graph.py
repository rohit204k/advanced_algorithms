class Graph:
    def __init__(self, vertices, edges, weights=None) -> None:
        self.v = vertices
        self.e = {}
        if weights is None:
            weights = [1]*len(edges)

        for i in range(len(edges)):
            self.e[edges[i]] = weights[i]

        self.adjacency_matrix = [[0] * len(self.v) for _ in range(len(self.v))]
        
        for (u, v), weight in self.e.items():
            self.adjacency_matrix[u - 1][v - 1] = weight
            self.adjacency_matrix[v - 1][u - 1] = weight
            

    def __str__(self):

        matrix_str = "  " + " ".join(map(str, self.v)) + "\n"
        
        for i in range(len(self.v)):
            matrix_str += str(self.v[i]) + " " + " ".join(map(str, self.adjacency_matrix[i])) + "\n"
        
        return matrix_str