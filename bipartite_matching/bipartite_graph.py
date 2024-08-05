from collections import deque, defaultdict


class BipartiteGraph:
    def __init__(self, U, V, edges, weights=None) -> None:
        self.U = U
        self.V = V
        self.e = {}
        if weights is None:
            weights = [1] * len(edges)

        for i in range(len(edges)):
            self.e[edges[i]] = weights[i]

        self.adjacency_matrix = self.create_adjacency_matrix()
        self.adjacency_list = self.create_adjacency_list()

    def update_edge_parameters(self):
        self.adjacency_matrix = self.create_adjacency_matrix()
        self.adjacency_list = self.create_adjacency_list()

    def create_adjacency_matrix(self):
        # Initialize the adjacency matrix with zeros
        matrix = [[0] * len(self.V) for _ in range(len(self.U))]

        # Fill the adjacency matrix with weights
        for (u, v), weight in self.e.items():
            u_index = self.U.index(u)
            v_index = self.V.index(v)
            matrix[u_index][v_index] = weight

        return matrix

    def create_adjacency_list(self):
        adj_list = defaultdict(list)
        for (u, v), _ in self.e.items():
            adj_list[u].append(v)
            # adj_list[v].append(u)  # if the graph is undirected
        return adj_list

    def __str__(self):
        matrix_str = "  " + " ".join(map(str, self.V)) + "\n"

        for i, row in enumerate(self.adjacency_matrix):
            matrix_str += str(self.U[i]) + " " + " ".join(map(str, row)) + "\n"

        return matrix_str
